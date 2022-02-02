from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from django_filters.rest_framework import DjangoFilterBackend
from posts.models import Follow, Group, Post
from rest_framework import filters, mixins, permissions, viewsets
from rest_framework.pagination import LimitOffsetPagination

from api.serializers import (CommentSerializer, FollowSerializer,
                             GroupSerializer, PostSerializer, UserSerializer)

from .permissions import OwnerOrReadOnly


class ListModelViewSet(mixins.ListModelMixin, mixins.RetrieveModelMixin,
                       viewsets.GenericViewSet):
    pass


class CreateorListViewSet(mixins.CreateModelMixin, mixins.ListModelMixin,
                          viewsets.GenericViewSet):
    pass


class UserViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    pagination_class = LimitOffsetPagination
    permission_classes = (OwnerOrReadOnly,)

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class GroupViewSet(ListModelViewSet):
    pagination_class = None
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


class FollowViewSet(CreateorListViewSet):
    permission_classes = (OwnerOrReadOnly, permissions.IsAuthenticated)
    serializer_class = FollowSerializer
    filter_backends = (DjangoFilterBackend, filters.SearchFilter)
    pagination_class = None
    search_fields = ('following__username', )

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def get_queryset(self):
        post_instance = Follow.objects.filter(user=self.request.user)
        return post_instance


class CommentViewSet(viewsets.ModelViewSet):
    serializer_class = CommentSerializer
    pagination_class = None
    permission_classes = (OwnerOrReadOnly,)

    def get_queryset(self):
        post_instance = get_object_or_404(Post, id=self.kwargs['id'])
        return post_instance.comments.all()

    def perform_create(self, serializer):
        post_instance = get_object_or_404(Post, id=self.kwargs['id'])
        serializer.save(author=self.request.user, post=post_instance)

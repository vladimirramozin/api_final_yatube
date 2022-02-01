from django.conf import settings
from django.conf.urls.static import static
from django.urls import include, path
from rest_framework.authtoken import views
from rest_framework.routers import DefaultRouter, SimpleRouter

from api.views import CommentViewSet, FollowViewSet, GroupViewSet, PostViewSet

app_name = 'api'
router_v1 = DefaultRouter()
router_v1.register(r'v1/posts', PostViewSet)
router_v1.register(r'v1/posts/(?P<id>\d+)/comments', CommentViewSet,
                   basename='id')
router_v1.register(r'v1/groups', GroupViewSet)
router_v1.register('v1/follow', FollowViewSet, basename='follow')
urlpatterns = [
    path('', include(router_v1.urls)),
    path('v1/', include('djoser.urls')),
    path('v1/', include('djoser.urls.jwt')),
]



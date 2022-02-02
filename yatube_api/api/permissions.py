from rest_framework import permissions


class OwnerOrReadOnly(permissions.BasePermission):

    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return request.method in permissions.SAFE_METHODS
        return obj.author == request.user


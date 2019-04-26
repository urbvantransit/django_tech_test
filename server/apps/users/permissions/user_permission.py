from rest_framework import permissions


class UserPermission(permissions.BasePermission):

    def has_permission(self, request, view):
        # permission = request.user.permissions.permission.option
        return request.method in permissions.SAFE_METHODS

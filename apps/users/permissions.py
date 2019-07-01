from rest_framework import permissions

from apps.users.models import UserPermissionModel


class ViewerPermission(permissions.BasePermission):

    def has_permission(self, request, view):

        return request.method in permissions.SAFE_METHODS and \
            request.user.is_authenticated


class EditorPermission(permissions.BasePermission):

    def has_permission(self, request, view):

        perm = request.user.permissions.permission

        if request.method == 'DELETE':
            return False

        allowed_perms = [
            UserPermissionModel.PERMISSIONS.get_value('editor'),
            UserPermissionModel.PERMISSIONS.get_value('owner'),
        ]

        return perm in allowed_perms


class OwnerPermission(permissions.BasePermission):

    def has_permission(self, request, view):

        perm = request.user.permissions.permission

        return perm == UserPermissionModel.PERMISSIONS.get_value('owner')

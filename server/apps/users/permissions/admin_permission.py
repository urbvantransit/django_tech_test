from rest_framework import permissions
from users.models import Permission


class AdminPermission(permissions.BasePermission):

    def has_permission(self, request, view):
        permission = request.user.permissions.permission.option
        return permission == Permission.ADMIN

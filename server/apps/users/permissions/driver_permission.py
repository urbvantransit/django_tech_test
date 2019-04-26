from rest_framework import permissions
from users.models import Permission


class DriverPermission(permissions.BasePermission):

    def has_permission(self, request, view):
        permission = request.user.permissions.permission.option
        method = request.method
        return (permission == Permission.DRIVER or
                method == 'PUT') or method in permissions.SAFE_METHODS

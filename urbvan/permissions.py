from rest_framework import permissions


class UserPermission(permissions.IsAuthenticated):

    def has_permission(self, request, view):
        if request.user.is_active:
            return True
        else:
            return False


class StaffUserPermission(UserPermission):

    def has_permission(self, request, view):
        if request.user.is_staff:
            return True
        else:
            return False


class AdminUserPermission(StaffUserPermission):

    def has_permission(self, request, view):
        if request.user.is_superuser:
            return True
        else:
            return False

# coding: utf8
from rest_framework.permissions import BasePermission, SAFE_METHODS


class UserReadPermission(BasePermission):
    """
    Only read permissions for user
    """

    def has_permission(self, request, view):
        user = request.user
        method = request.method
        return user and user.is_authenticated and method in SAFE_METHODS


class StaffUserPermission(BasePermission):
    """
    Only Staff users
    """

    def has_permission(self, request, view):
        return request.user and request.user.is_staff


class SuperUserPermission(BasePermission):
    """
    Only super users
    """

    def has_permission(self, request, view):
        return request.user and request.user.is_superuser

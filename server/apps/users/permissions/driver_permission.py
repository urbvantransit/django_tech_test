# coding: utf-8
from rest_framework import permissions

from apps.users.models import UserPermission


class DriverPermission(permissions.BasePermission):

    def has_permission(self, request, view):
        permission = request.user.permissions.option
        method = request.method

        return (permission == UserPermission.DRIVER and
                method in ['PUT', 'PATCH']) or \
            method in permissions.SAFE_METHODS or \
            permission == UserPermission.ADMIN

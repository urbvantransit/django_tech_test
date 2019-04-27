# coding: utf-8
from rest_framework import permissions

from apps.users.models import UserPermission


class AdminPermission(permissions.BasePermission):

    def has_permission(self, request, view):
        permission = request.user.permissions.option
        return permission == UserPermission.ADMIN

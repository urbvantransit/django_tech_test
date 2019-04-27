# coding: utf-8
from rest_framework import permissions


class UserPermission(permissions.BasePermission):

    def has_permission(self, request, view):
        return request.method in permissions.SAFE_METHODS

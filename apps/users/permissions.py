# coding: utf8
from rest_framework.permissions import SAFE_METHODS, BasePermission


class CustomPermission(BasePermission):
    """Custom DRF permissions class for urbvan test

    Implements 3 leves of access:
        - Anonymous: no access
        - Authenticated: read only
        - Staff: full access
    """

    def has_permission(self, request, view):
        if request.method in SAFE_METHODS:
            return request.user and request.user.is_authenticated
        else:
            return request.user and request.user.is_authenticated and request.user.is_staff

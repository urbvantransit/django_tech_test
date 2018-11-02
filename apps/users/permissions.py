from rest_framework.permissions import BasePermission


class BasicUser(BasePermission):
    """ Most basic user, only have access to read some data """

    def has_permission(self, request, view):
        return request.user and request.user.is_authenticated


class StaffUser(BasePermission):
    """ Staff member, can get, create and update data """
    def has_permission(self, request, view):
        return request.user and request.user.is_staff


class SuperUser(BasePermission):
    """ Superuser has access to all the actions of the CRUD """
    def has_permission(self, request, view):
        return request.user and request.user.is_superuser

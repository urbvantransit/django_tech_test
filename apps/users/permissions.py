from rest_framework.permissions import BasePermission


class IsTier2(BasePermission):
    """ Tier2, can get, create and update data """
    def has_permission(self, request, view):
        return request.user and (request.user.is_tier2 or \
            request.user.is_tier3)


class IsTier3(BasePermission):
    """ Tier3 has access to all the actions of the CRUD """
    def has_permission(self, request, view):
        return request.user and request.user.is_tier3

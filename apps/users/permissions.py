from rest_framework import permissions

class IsNormalUser(permissions.BasePermission):
    
    def has_permission(self, request, view):
        if request.user and request.user.profile.user_type >= 0:
            return True
        else:
            return False

class IsAdminUser(permissions.BasePermission):
    
    def has_permission(self, request, view):
        if request.user and request.user.profile.user_type >= 1:
            return True
        else:
            return False


class IsSuperAdminUser(permissions.BasePermission):

    def has_permission(self, request, view):
        if request.user and request.user.profile.user_type == 2:
            return True
        else:
            return False

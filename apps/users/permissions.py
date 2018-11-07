from rest_framework import permissions

class CustomPermissions(permissions.BasePermission):
    """
    Permisos personalizados para cada método y grupo de usuarios
    """

    def has_object_permission(self, request, view, obj):
        user = request.user
        if user:
            if user.is_superuser:
                return True
            else:
                # 'GET', 'OPTIONS' or 'HEAD'
                if request.method in permissions.SAFE_METHODS and user.groups.filter(id__in=[1,3]).exists():
                    return True
                # 'PUT', 'PATCH'
                elif request.method in ["PUT", "PATCH"] and user.groups.filter(id__in=[2,3]).exists():
                    return True
                # 'DELETE'   
                elif request.method == "DELETE" and user.groups.filter(id__in=[3,4]).exists():
                    return True
        return False
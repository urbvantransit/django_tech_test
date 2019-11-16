# Aquí se almacenan los decoradores necesarios para añadir
# una capa de seguridad a las vistas/endpoints de la api
# estos decoradores añaden permisos a los endpoints,
# en caso de que un usuario no pase la prueba con 
# `user_passes_test`, retorna `False` y por ende, lo rechaza
# y quiere decir que no tiene permisos para hacer x o y acción

from django.contrib.auth.decorators import user_passes_test
from django.core.exceptions import PermissionDenied


def group_required(*group_name):
    """
    Requiere que para hacer la acción que se pretende,
    el usuario debe estar en un grupo específico.
    """
    def in_groups(u):
        if u.is_authenticated():
            if bool(u.groups.filter(name__in=group_name)) | u.is_superuser:
                return True
        return False
    return user_passes_test(in_groups) 


def superuser_only(function):
    """
    Lmita la vista únicamente a los super usuarios
    """

    def _inner(request, *args, **kwargs):
        if not request.user.is_superuser:
            raise PermissionDenied           
        return function(request, *args, **kwargs)
    return _inner

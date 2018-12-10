# coding: utf8

from rest_framework import permissions


class ModelCRUDPermission(permissions.BasePermission):
    """
    CRUD Model Permissions
    ----------------------

    CRUD Model Permissions is a Group / Role - based permission system for
    CRUD actions on Models which requires no additional queries to the
    database (no database overhead, no penality on performance).

    It is intended to be used in the Models' CRUD endpoints of the REST API.

    It stores the user's group or role in a field called 'user_type' in the
    User model (requires the project to be using a Custom User Model) and
    the user types are defined / configured in users_types.py module of the
    Users app.

    In each model that the permission check is desired, the constant
    MODEL_CRUD_PERMISSIONS needs to be defined in the following way::

        from apps.users.user_types import USER_TYPES as UT

        class MyModel(models.Model):
            ...
            MODEL_CRUD_PERMISSIONS = {
                "create": [ UT["supervisor"], UT["driver"] ], 
                "retrieve": [ 
                    UT["supervisor"], UT["driver"], UT["passenger"]
                ],
                "update": [ UT["supervisor"], UT["driver"] ], 
                "delete": [ UT["supervisor"], UT["driver"] ], 
            }
            ...

    Then for each Class-Based View, you have to specify the model which
    contains the permissions for the actions in the 'model_crud_permissions'
    attribute and set (or make it inherit) the permission classes,
    for example::


        class MyModelView(ListCreateView):

            ...
            model_crud_permissions = MyModel
            permission_classes = (IsAuthenticated, ModelCRUDPermission, ...)
            ...

    When a User performs a request, if the User Type is listed in the types
    allowed to perform the action requested, it returns True - and false
    otherwise (except for Staff and Super users are always allowed to perform
    CRUD actions).

    If the 'model_crud_permissions' is not set in the view or
    MODEL_CRUD_PERMISSION is not set in the model it returns True as
    assumes that the check is not intended for the view or model.
    """

    PERMS_MAP = {
        # Maps HTTP verbs to CRUD actions
        'GET': 'retrieve',
        'OPTIONS': 'retrieve',
        'HEAD': 'retrieve',
        'POST': 'create',
        'PUT': 'update',
        'PATCH': 'update',
        'DELETE': 'delete',
    }

    def has_permission(self, request, view):
        """
        Checks that the (CB)View has the 'model_crud_permissions' attribute
        defined which should contain the constant MODEL_CRUD_PERMISSIONS
        in which the User Types allowed to perform the CRUD actions are listed
        """
        if (getattr(view, 'model_crud_permissions', None) and
                getattr(view.model_crud_permissions,
                'MODEL_CRUD_PERMISSIONS', None)):
            if request.user.is_staff or request.user.is_superuser:
                # Allow staff and superuser users
                return True
            else:
                try:
                    perms = view.model_crud_permissions.MODEL_CRUD_PERMISSIONS
                    if (request.user.user_type in 
                            perms[self.PERMS_MAP[request.method]]):
                        return True
                    else:
                        return False
                except Exception as e:
                    # If something goes wrong like MODEL_CRUD_PERMISSIONS is
                    # not defined as expected (other format, method missing, etc.)
                    # deny the permission.
                    return False
        else:
            # Model CRUD Permissions is disabled for the view or model
            return True

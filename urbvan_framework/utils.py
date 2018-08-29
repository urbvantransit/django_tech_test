# coding: utf8
from urbvan_framework.schemas import (BaseResponseSchema, BaseBodySchema)
from urbvan import permissions


def render_response_error(errors={}):
    list_errors = []
    for key, value in errors.items():

        if type(value) is list:
            value = {"message": value[0]}
        value.update({"field": key})
        list_errors.append(value)

    response = {"errors": list_errors}

    response = BaseResponseSchema().dump(response).data
    return response


def render_to_response(body={}):

    response = {}
    response = BaseBodySchema().dump({
        "result": body
    }).data
    response = BaseResponseSchema().dump({
        "body": response
    }).data

    return response


def get_urbvan_permissions(action):
    if action == 'destroy':
        permission_classes = [permissions.AdminUserPermission]
    elif action == 'create':
        permission_classes = [permissions.StaffUserPermission]
    elif action == 'partial_update':
        permission_classes = [permissions.StaffUserPermission]
    else:
        permission_classes = [permissions.UserPermission]

    return [permission() for permission in permission_classes]

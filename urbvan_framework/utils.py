from .schemas import (BaseResponseSchema, BaseBodySchema)


def error_builder_for_render(exception):
    '''
    Build exception error for render_response_error
    :param exception: Exception Object
    :return: Base error message
    '''
    if hasattr(exception, 'detail'):
        error = exception.detail
    else:
        error = {"base": {"message": str(exception)}}

    return error


def render_response_error(errors={}):
    list_errors = []
    for key, value in errors.items():

        if isinstance(value, list):
            value = {"message": value[0]}

        value.update({"field": key})
        list_errors.append(value)

    response = {"errors": list_errors}

    response = BaseResponseSchema().dump(response).data
    return response


def render_to_response(body={}):

    response = {}
    response = BaseBodySchema().dump({
        "results": [body]
    }).data
    response = BaseResponseSchema().dump({
        "body": response
    }).data

    return response

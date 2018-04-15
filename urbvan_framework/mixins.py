# coding: utf8
from rest_framework import (mixins, status)
from rest_framework.response import Response

from .utils import (render_to_response, render_response_error)


class CreateModelMixin(mixins.CreateModelMixin):

    def create(self, request, *args, **kwargs):

        serializer = self.get_serializer(data=request.data)

        if not serializer.is_valid():
            response = render_response_error(errors=serializer.errors)
            return Response(response, status=status.HTTP_400_BAD_REQUEST)

        try:
            self.perform_create(serializer)
        except Exception as e:
            if hasattr(e, 'detail'):
                error = e.detail
            else:
                error = {"base": {"message": str(e)}}

            response = render_response_error(errors=error)
            return Response(response, status=status.HTTP_400_BAD_REQUEST)

        instance = serializer.instance

        schema = self.schema_class()
        schema = schema.dump(instance).data

        response = render_to_response(body=schema)

        return Response(response, status=status.HTTP_201_CREATED)


class ListModelMixin(object):

    def list(self, request, *args, **kwargs):

        queryset = self.get_queryset()
        queryset = self.filter_queryset(queryset)

        page = self.paginate_queryset(queryset)
        schema = self.schema_class(many=True)

        schema = schema.dump(page).data

        return self.get_paginated_response(schema)

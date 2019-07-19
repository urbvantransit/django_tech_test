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


class ListModelMixin(mixins.ListModelMixin):

    def list(self, request, *args, **kwargs):

        queryset = self.get_queryset()
        queryset = self.filter_queryset(queryset)

        page = self.paginate_queryset(queryset)
        schema = self.schema_class(many=True).dump(page)

        return self.get_paginated_response(schema.data)


class RetrieveModelMixin(mixins.RetrieveModelMixin):

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)

        response = render_to_response(body=serializer.data)

        return Response(response)


class UpdateModelMixin(mixins.UpdateModelMixin):

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        is_partial = kwargs.pop('partial', False)

        serializer = self.get_serializer(
            instance,
            data=request.data,
            partial=is_partial
        )

        serializer.is_valid(raise_exception=True)

        self.perform_update(serializer)

        if getattr(instance, '_prefetched_objects_cache', None):
            instance._prefetched_objects_cache = {}

        schema = self.schema_class().dump(instance)

        response = render_to_response(body=schema.data)

        return Response(response)

    def perform_update(self, serializer):
        serializer.save()

    def partial_update(self, request, *args, **kwargs):
        kwargs['partial'] = True
        return self.update(request, *args, **kwargs)


# coding: utf8
from rest_framework import (mixins, status)
from rest_framework.response import Response

from urbvan_framework.utils import (render_to_response, render_response_error)


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


class RetrieveModelMixin(mixins.RetrieveModelMixin):

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        schema = self.schema_class()

        schema = schema.dump(instance).data

        response = render_to_response(body=schema)

        return Response(response, status=status.HTTP_200_OK)


class DestroyModelMixin(mixins.DestroyModelMixin):

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response(status=status.HTTP_204_NO_CONTENT)

    def perform_destroy(self, instance):
        instance.delete()


class UpdateModelMixin(mixins.UpdateModelMixin):

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', True)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)

        if not serializer.is_valid():
            response = render_response_error(errors=serializer.errors)
            return Response(response, status=status.HTTP_400_BAD_REQUEST)

        try:
            self.perform_update(serializer)
        except Exception as e:
            if hasattr(e, 'detail'):
                error = e.detail
            else:
                error = {"base": {"message": str(e)}}

            response = render_response_error(errors=error)
            return Response(response, status=status.HTTP_400_BAD_REQUEST)

        instance = serializer.instance

        if getattr(instance, '_prefetched_objects_cache', None):
            # If 'prefetch_related' has been applied to a queryset, we need to
            # forcibly invalidate the prefetch cache on the instance.
            instance._prefetched_objects_cache = {}

        schema = self.schema_class()
        schema = schema.dump(instance).data

        response = render_to_response(body=schema)

        return Response(response, status=status.HTTP_200_OK)

    def perform_update(self, serializer):
        serializer.save()

    def partial_update(self, request, *args, **kwargs):
        kwargs['partial'] = True
        return self.update(request, *args, **kwargs)

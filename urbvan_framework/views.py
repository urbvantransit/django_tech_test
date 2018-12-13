# coding: utf8
from django.http import Http404
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from .mixins import (
    CreateModelMixin,
    ListModelMixin,
    RetrieveModelMixin,
    UpdateModelMixin,
    DestroyModelMixin)
from .schemas import PaginationResponse
from .authentication import CustomTokenAuthentication


class CreateAPIView(CreateModelMixin, generics.GenericAPIView):
    """
    Concrete view for creating a model instance.
    """
    authentication_classes = (CustomTokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class ListAPIView(ListModelMixin, generics.GenericAPIView):
    """
    Concrete view for listing a queryset.
    """

    authentication_classes = (CustomTokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    pagination_class = PaginationResponse

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)


class ListCreateView(CreateAPIView, ListAPIView):
    pass


class DetailView(generics.RetrieveUpdateDestroyAPIView):
    """
    Concrete view for Retrieve, update or delete an instance with permissions.
    """
    authentication_classes = (CustomTokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return super().put(request, *args, **kwargs)

    def patch(self, request, *args, **kwargs):
        return super().patch(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return super().delete(request, *args, **kwargs)

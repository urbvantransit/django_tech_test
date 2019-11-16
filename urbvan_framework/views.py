# coding: utf8
from rest_framework import mixins
from rest_framework.generics import GenericAPIView
from rest_framework.permissions import IsAuthenticated

from .authentication import CustomTokenAuthentication
from .mixins import (
    CreateModelMixin, ListModelMixin, RetrieveModelMixin, UpdateModelMixin)
from .schemas import PaginationResponse


class CreateAPIView(CreateModelMixin, GenericAPIView):
    """
    Concrete view for creating a model instance.
    """
    authentication_classes = (CustomTokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class ListAPIView(ListModelMixin, GenericAPIView):
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

class RetrieveView(RetrieveModelMixin, GenericAPIView):
    """
    Vista concreta para obtener un objeto, en este caso 
    una `Line` pasandole el id de la linea.
    """

    authentication_classes = (CustomTokenAuthentication, )
    permission_classes = (IsAuthenticated, )

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

class UpdateView(UpdateModelMixin, GenericAPIView):

    authentication_classes = (CustomTokenAuthentication, )
    permission_classes = (IsAuthenticated, )

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def patch(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)

class DestroyView(mixins.DestroyModelMixin,
                     GenericAPIView):
    authentication_classes = (CustomTokenAuthentication, )
    permission_classes = (IsAuthenticated, )
    """
    Concrete view for deleting a model instance.
    """
    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)

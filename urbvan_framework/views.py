# coding: utf8
from rest_framework.generics import GenericAPIView,\
                                                       UpdateAPIView,\
                                                       DestroyAPIView
from rest_framework.permissions import IsAuthenticated

from .mixins import CreateModelMixin, ListModelMixin
from .schemas import PaginationResponse
from .authentication import CustomTokenAuthentication


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


class UpdateView(UpdateAPIView, GenericAPIView):
    """
    Concrete view for update a model instance.
    """
    authentication_classes = (CustomTokenAuthentication,)
    permission_classes = (IsAuthenticated,)
    pagination_class = PaginationResponse

    def patch(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)


class DestroyView(DestroyAPIView, GenericAPIView):
    """
    Concrete view for delete a model instance.
    """
    authentication_classes = (CustomTokenAuthentication,)
    permission_classes = (IsAuthenticated,)
    pagination_class = PaginationResponse

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)

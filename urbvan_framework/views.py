# coding: utf8
# THIRD-PARTY IMPORTS
from rest_framework.generics import GenericAPIView
from rest_framework.permissions import IsAuthenticated

# URBVAN IMPORTS
from .mixins import (
    CreateModelMixin,
    ListModelMixin,
    RetrieveModelMixin,
    UpdateModelMixin,
    DestroyModelMixin,
)
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


class RetrieveView(RetrieveModelMixin, GenericAPIView):
    '''
        A view to retrieve a model instance
        @author Christian Buendia
    '''

    authentication_classes = (CustomTokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)


class UpdateView(UpdateModelMixin, GenericAPIView):
    '''
        A view to update a model instance
        @author Christian Buendia
    '''

    authentication_classes = (CustomTokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)


class DeleteView(DestroyModelMixin, GenericAPIView):
    '''
        A view to delete a model instance
        @author Christian Buendia
    '''

    authentication_classes = (CustomTokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)


class RetrieveUpdateDeleteView(RetrieveView, UpdateView, DeleteView):
    pass
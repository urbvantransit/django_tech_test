from rest_framework.generics import GenericAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import GenericViewSet

from .authentication import CustomTokenAuthentication
from .mixins import (
    CreateModelMixin, ListModelMixin,
    RetrieveModelMixin, UpdateModelMixin
)
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


class RetrieveAPIView(RetrieveModelMixin, GenericAPIView):
    """
    APIView to retrieve a model instance
    """
    authentication_classes = (CustomTokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)


class UpdateAPIView(UpdateModelMixin, GenericAPIView):
    """
    APIView to update a single model instance
    """

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def patch(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)


class ReadViewSet(ListAPIView, RetrieveAPIView, GenericViewSet):
    """
    Read only view set
    Created only for List & Retrieve available methods
    (GET method)
    """
    pass


class WriteViewSet(CreateAPIView, UpdateAPIView, GenericViewSet):
    """
    Write only view set
    Created only for Create & Update available methods
    (POST, PUT, PATCH, Method)
    """
    pass

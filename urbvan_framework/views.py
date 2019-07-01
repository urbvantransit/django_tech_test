from rest_framework.generics import GenericAPIView, DestroyAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import GenericViewSet

from apps.users.permissions import ViewerPermission, EditorPermission, OwnerPermission
from .mixins import (
    CreateModelMixin,
    ListModelMixin,
    RetrieveModelMixin,
    UpdateModelMixin,
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


class RetrieveAPIView(RetrieveModelMixin, GenericAPIView):

    authentication_classes = (CustomTokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)


class UpdateAPIView(UpdateModelMixin, GenericAPIView):

    authentication_classes = (CustomTokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def patch(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)


class ReadOnlyModelViewSet(ListAPIView, RetrieveAPIView, GenericViewSet):

    def get_permissions(self):
        if self.action in ('list', 'retrieve'):
            permission_classes = [ViewerPermission]
        return [permission() for permission in permission_classes]


class WriteOnlyModelViewSet(CreateAPIView, UpdateAPIView, DestroyAPIView, GenericViewSet):
    def get_permissions(self):
        if self.action in ('create', 'update', 'partial_update'):
            permission_classes = [EditorPermission]
        else:
            permission_classes = [OwnerPermission]
        return [permission() for permission in permission_classes]



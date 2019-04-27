# coding: utf-8
from rest_framework.generics import DestroyAPIView, GenericAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import GenericViewSet

from .mixins import (
    CreateModelMixin,
    ListModelMixin,
    RetrieveModelMixin,
    UpdateModelMixin
)
from .schemas import PaginationResponse
from .authentication import CustomTokenAuthentication
from apps.users.permissions import (
    AdminPermission,
    DriverPermission,
    UserPermission
)


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
    Concrete view for retrieving a model instance.
    """
    authentication_classes = (CustomTokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)


class UpdateAPIView(UpdateModelMixin, GenericAPIView):
    """
    Concrete view for updating a model instance.
    """

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def patch(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)


class RetrieveUpdateDestroyView(RetrieveAPIView,
                                UpdateAPIView,
                                DestroyAPIView,
                                GenericAPIView):
    pass


class ModelViewSet(
        CreateAPIView,
        ListAPIView,
        RetrieveAPIView,
        UpdateAPIView,
        DestroyAPIView,
        GenericViewSet):

    permission_classes_by_action = {
        'create': [AdminPermission],
        'list': [UserPermission],
        'retrieve': [UserPermission],
        'update': [DriverPermission],
        'partial_update': [DriverPermission],
        'destroy': [AdminPermission]
    }

    def get_permissions(self):
        try:
            # return permission_classes depending on `action`
            return [permission()
                    for permission in self.permission_classes_by_action[
                        self.action]]
        except KeyError:
            # action is not set return default permission_classes
            return [permission() for permission in self.permission_classes]

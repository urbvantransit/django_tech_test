# coding: utf8
from rest_framework.generics import GenericAPIView
from rest_framework.permissions import IsAuthenticated, BasePermission

from .mixins import (CreateModelMixin, ListModelMixin)
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


class IsSuperUser(BasePermission):
    """
    Allows access only to superusers for (CRUD)
    """
    def has_permission(self, request, view):
        return request.user.is_superuser


class IsAnonymousUser(BasePermission):
    """
    Allows access only to  users only for read
    """
    def has_permission(self, request, view):
        return request.user.is_anonymous or request.user.is_superuser or request.user.is_staff


class IsStaffUser(BasePermission):
    """
    Allows access only to staff users for update models

    """

    def has_permission(self, request, view):
        return request.user and request.user.is_superuser or request.user.is_staff

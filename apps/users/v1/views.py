from django.contrib.auth.models import User
from rest_framework import viewsets

from apps.users.v1.serializers import UserSerializer
from apps.users.v1.schemas import UserSchema
from urbvan_framework.views import CRUDLView
from urbvan_framework.utils import get_urbvan_permissions


class UserViewSet(CRUDLView, viewsets.GenericViewSet):
    queryset = User.objects.all().order_by('pk')
    serializer_class = UserSerializer
    schema_class = UserSchema

    def get_permissions(self):
        return get_urbvan_permissions(self.action)

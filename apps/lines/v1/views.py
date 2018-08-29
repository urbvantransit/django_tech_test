from rest_framework import viewsets

from apps.lines.models import LineModel, RouteModel
from apps.lines.v1.serializers import LineSerializer, RouteSerializer
from apps.lines.v1.schemas import LineSchema, RouteSchema
from urbvan_framework.views import CRUDLView
from urbvan_framework.utils import get_urbvan_permissions


class LineViewSet(CRUDLView, viewsets.GenericViewSet):
    queryset = LineModel.objects.all()
    serializer_class = LineSerializer
    schema_class = LineSchema

    def get_permissions(self):
        return get_urbvan_permissions(self.action)


class RouteViewSet(CRUDLView, viewsets.GenericViewSet):
    queryset = RouteModel.objects.all()
    serializer_class = RouteSerializer
    schema_class = RouteSchema

    def get_permissions(self):
        return get_urbvan_permissions(self.action)

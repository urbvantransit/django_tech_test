from rest_framework import viewsets

from apps.lines.models import LineModel, RouteModel
from apps.lines.v1.serializers import LineSerializer, RouteSerializer
from apps.lines.v1.schemas import LineSchema, RouteSchema
from urbvan_framework.views import CRUDLView


class LineViewSet(CRUDLView, viewsets.GenericViewSet):
    queryset = LineModel.objects.all()
    serializer_class = LineSerializer
    schema_class = LineSchema


class RouteViewSet(CRUDLView, viewsets.GenericViewSet):
    queryset = RouteModel.objects.all()
    serializer_class = RouteSerializer
    schema_class = RouteSchema

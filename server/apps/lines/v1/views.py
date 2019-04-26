# coding: utf-8
from urbvan_framework.views import ModelViewSet

from apps.lines.v1.schemas import LineSchema, RouteSchema
from apps.lines.v1.serializers import LineSerializer, RouteSerializer

from apps.lines.models import LineModel, RouteModel


class LineModelViewSet(ModelViewSet):

    queryset = LineModel.objects.all()
    schema_class = LineSchema
    serializer_class = LineSerializer


class RouteModelViewSet(ModelViewSet):

    queryset = RouteModel.objects.prefetch_related(
        'stations').select_related('line').all()
    schema_class = RouteSchema
    serializer_class = RouteSerializer

# coding: utf-8
from urbvan_framework.views import ListCreateView, RetrieveUpdateDestroyView

from apps.lines.v1.schemas import LineSchema, RouteSchema
from apps.lines.v1.serializers import LineSerializer, RouteSerializer

from apps.lines.models import LineModel, RouteModel


class LineListCreateView(ListCreateView):

    queryset = LineModel.objects.all()
    schema_class = LineSchema
    serializer_class = LineSerializer


class RouteListCreateView(ListCreateView):

    queryset = RouteModel.objects.prefetch_related(
        'stations').select_related('line').all()
    schema_class = RouteSchema
    serializer_class = RouteSerializer


class LineRetrieveUpdateDeleteView(RetrieveUpdateDestroyView):

    queryset = LineModel.objects.all()
    schema_class = LineSchema
    serializer_class = LineSerializer


class RouteRetrieveUpdateDeleteView(RetrieveUpdateDestroyView):

    queryset = RouteModel.objects.prefetch_related(
        'stations').select_related('line').all()
    schema_class = RouteSchema
    serializer_class = RouteSerializer

from apps.lines.models import LineModel, RouteModel
from apps.lines.v1.schemas import LineSchema, RouteSchema
from apps.lines.v1.serializers import LineSerializer, RouteSerializer
from urbvan_framework.views import ReadOnlyModelViewSet, WriteOnlyModelViewSet


class ReadOnlyLineViewSet(ReadOnlyModelViewSet):

    queryset = LineModel.objects.all()
    schema_class = LineSchema
    serializer_class = LineSerializer


class WriteOnlyLineViewSet(WriteOnlyModelViewSet):

    queryset = LineModel.objects.all()
    schema_class = LineSchema
    serializer_class = LineSerializer


class ReadOnlyRouteViewSet(ReadOnlyModelViewSet):

    queryset = RouteModel.objects.all()
    schema_class = RouteSchema
    serializer_class = RouteSerializer


class WriteOnlyRouteViewSet(WriteOnlyModelViewSet):

    queryset = RouteModel.objects.all()
    schema_class = RouteSchema
    serializer_class = RouteSerializer


from apps.lines.models import (LineModel, RouteModel)
from apps.lines.v1.schemas import (LineSchema, RouteSchema)
from apps.lines.v1.serializers import (LineSerializer, RouteSerializer)

from urbvan_framework.views import (ReadOnlyModelViewSet, WriteOnlyModelViewSet)


class LineReadViewSet(ReadOnlyModelViewSet):
    """
    Concrete ViewSet for LineModel reading methods
    """
    queryset = LineModel.objects.all()

    schema_class = LineSchema
    serializer_class = LineSerializer


class LineWriteViewSet(WriteOnlyModelViewSet):
    """
    Concrete ViewSet for LineModel write methods
    """
    queryset = LineModel.objects.all()
    schema_class = LineSchema
    serializer_class = LineSerializer


class RouteReadViewSet(ReadOnlyModelViewSet):
    """
    Concrete ViewSet for RouteModel reading methods
    """
    queryset = RouteModel.objects.all()
    schema_class = RouteSchema
    serializer_class = RouteSerializer


class RouteWriteViewSet(WriteOnlyModelViewSet):
    """
    Concrete ViewSet for RouteModel write methods
    """
    queryset = RouteModel.objects.all()
    schema_class = RouteSchema
    serializer_class = RouteSerializer

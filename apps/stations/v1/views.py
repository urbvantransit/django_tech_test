from urbvan_framework.views import ReadOnlyModelViewSet, WriteOnlyModelViewSet

from .schemas import LocationSchema, StationSchema
from .serializers import LocationSerializer, StationSerializer

from ..models import LocationModel, StationModel


class ReadOnlyLocationViewSet(ReadOnlyModelViewSet):

    queryset = LocationModel.objects.all()
    schema_class = LocationSchema
    serializer_class = LocationSerializer


class WriteOnlyLocationViewSet(WriteOnlyModelViewSet):

    queryset = LocationModel.objects.all()
    schema_class = LocationSchema
    serializer_class = LocationSerializer


class ReadOnlyStationViewSet(ReadOnlyModelViewSet):

    queryset = StationModel.objects.all()
    schema_class = StationSchema
    serializer_class = StationSerializer


class WriteOnlyStationViewSet(WriteOnlyModelViewSet):

    queryset = StationModel.objects.all()
    schema_class = StationSchema
    serializer_class = StationSerializer




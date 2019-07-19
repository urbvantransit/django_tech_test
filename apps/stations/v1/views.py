from urbvan_framework.views import (ReadViewSet, WriteViewSet)

from .schemas import (LocationSchema, StationSchema)
from .serializers import (LocationSerializer, StationSerializer)

from ..models import LocationModel, StationModel


class LocationReadViewSet(ReadViewSet):
    queryset = LocationModel.objects.all()
    schema_class = LocationSchema
    serializer_class = LocationSerializer


class LocationWriteViewSet(WriteViewSet):
    queryset = LocationModel.objects.all()
    schema_class = LocationSchema
    serializer_class = LocationSerializer


class StationReadViewSet(ReadViewSet):
    queryset = StationModel.objects.all()
    schema_class = StationSchema
    serializer_class = StationSerializer


class StationWriteViewSet(WriteViewSet):
    queryset = StationModel.objects.all()
    schema_class = StationSchema
    serializer_class = StationSerializer

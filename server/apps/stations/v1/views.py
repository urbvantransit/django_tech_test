# coding: utf-8
from urbvan_framework.views import ModelViewSet

from apps.stations.v1.schemas import LocationSchema, StationSchema
from apps.stations.v1.serializers import LocationSerializer, StationSerializer

from apps.stations.models import LocationModel, StationModel


class LocationModelViewSet(ModelViewSet):

    queryset = LocationModel.objects.all()
    schema_class = LocationSchema
    serializer_class = LocationSerializer
    # permission_classes =


class StationModelViewSet(ModelViewSet):

    queryset = StationModel.objects.select_related('location').all()
    schema_class = StationSchema
    serializer_class = StationSerializer

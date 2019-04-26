# coding: utf-8
from urbvan_framework.views import ListCreateView, RetrieveUpdateDestroyView

from apps.stations.v1.schemas import LocationSchema, StationSchema
from apps.stations.v1.serializers import LocationSerializer, StationSerializer

from apps.stations.models import LocationModel, StationModel


class LocationListCreateView(ListCreateView):

    queryset = LocationModel.objects.all()
    schema_class = LocationSchema
    serializer_class = LocationSerializer


class StationListCreateView(ListCreateView):

    queryset = StationModel.objects.select_related('location').all()
    schema_class = StationSchema
    serializer_class = StationSerializer


class LocationRetrieveUpdateDeleteView(RetrieveUpdateDestroyView):

    queryset = LocationModel.objects.all()
    schema_class = LocationSchema
    serializer_class = LocationSerializer


class StationRetrieveUpdateDeleteView(RetrieveUpdateDestroyView):

    queryset = StationModel.objects.select_related('location').all()
    schema_class = StationSchema
    serializer_class = StationSerializer

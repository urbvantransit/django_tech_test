# coding: utf8
from rest_framework import viewsets

from apps.stations.v1.schemas import StationSchema, LocationSchema
from apps.stations.v1.serializers import StationSerializer, LocationSerializer
from apps.stations.models import StationModel, LocationModel
from urbvan_framework.views import CRUDLView


class LocationViewSet(CRUDLView, viewsets.GenericViewSet):

    queryset = LocationModel.objects.all()
    schema_class = LocationSchema
    serializer_class = LocationSerializer

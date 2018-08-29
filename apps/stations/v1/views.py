# coding: utf8
from rest_framework import viewsets

from apps.stations.v1.schemas import StationSchema, LocationSchema
from apps.stations.v1.serializers import StationSerializer, LocationSerializer
from apps.stations.models import StationModel, LocationModel
from urbvan_framework.views import CRUDLView
from urbvan_framework.utils import get_urbvan_permissions


class LocationViewSet(CRUDLView, viewsets.GenericViewSet):

    queryset = LocationModel.objects.all()
    schema_class = LocationSchema
    serializer_class = LocationSerializer

    def get_permissions(self):
        return get_urbvan_permissions(self.action)


class StationViewSet(CRUDLView, viewsets.GenericViewSet):

    queryset = StationModel.objects.all()
    schema_class = StationSchema
    serializer_class = StationSerializer

    def get_permissions(self):
        return get_urbvan_permissions(self.action)

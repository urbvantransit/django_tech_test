# coding: utf8
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from ...users.permissions import CustomPermissions

from .schemas import LocationSchema, StationSchema
from .serializers import LocationSerializer, StationSerializer

from ..models import LocationModel, StationModel


# Clase para recibir peticiones del modelo Locations
class LocationView(viewsets.ModelViewSet):
    queryset = LocationModel.objects.all()
    schema_class = LocationSchema
    serializer_class = LocationSerializer
    permission_classes = (CustomPermissions, IsAuthenticated)


# Clase para recibir peticiones del modelo Stations
class StationView(viewsets.ModelViewSet):
    queryset = StationModel.objects.all()
    schema_class = StationSchema
    serializer_class = StationSerializer
    permission_classes = (CustomPermissions, IsAuthenticated)
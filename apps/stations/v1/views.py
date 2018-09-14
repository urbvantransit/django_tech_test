# coding: utf8
from rest_framework.viewsets import ModelViewSet

from . import serializers
from .. import models


class LocationViewSet(ModelViewSet):
    queryset = models.LocationModel.objects.all()
    serializer_class = serializers.LocationSerializer


class StationViewSet(ModelViewSet):
    queryset = models.StationModel.objects.all()
    serializer_class = serializers.StationSerializer

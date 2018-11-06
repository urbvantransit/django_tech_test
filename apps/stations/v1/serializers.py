# coding: utf8
from rest_framework import serializers

from apps.stations.models import LocationModel, StationModel


class LocationSerializer(serializers.ModelSerializer):

    class Meta:
        model = LocationModel
        fields = ('id', 'name', 'latitude', 'longitude')


class StationSerializer(serializers.ModelSerializer):

    class Meta:
        model = StationModel
        fields = ('id', 'location', 'order', 'is_active')        
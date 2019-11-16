# coding: utf8
from rest_framework import serializers

from apps.stations.models import LocationModel, StationModel


class LocationSerializer(serializers.ModelSerializer):

    class Meta:
        model = LocationModel
        exclude = ('id', )
        read_only_fields = ('user', )

class StationSerializer(serializers.ModelSerializer):

    class Meta:
        model = StationModel
        exclude = ('id', )
        read_only_fields = ('user', )
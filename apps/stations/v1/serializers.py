# coding: utf8
from rest_framework import serializers

from apps.stations.models import LocationModel, StationModel 


class LocationSerializer(serializers.ModelSerializer):

    class Meta:
        model = LocationModel
        exclude = ('id', )


class LocationSerializerId(serializers.ModelSerializer):

    class Meta:
        model = LocationModel
        exclude = ()


class StationSerializer(serializers.ModelSerializer):

    class Meta:
        model = StationModel
        exclude = ('id', )


class StationSerializerId(serializers.ModelSerializer):

    class Meta:
        model = StationModel
        exclude = ()
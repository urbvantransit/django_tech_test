# coding: utf8
# THIRD-PARTY IMPORTS
from rest_framework import serializers

#URBVAN IMPORTS
from apps.stations.models import LocationModel, StationModel


class LocationSerializer(serializers.ModelSerializer):

    class Meta:
        model = LocationModel
        exclude = ('id', )


class StationSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = StationModel
        fields = '__all__'

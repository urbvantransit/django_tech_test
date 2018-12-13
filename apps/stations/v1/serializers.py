# coding: utf8
from rest_framework import serializers

from ..models import LocationModel,StationModel


class LocationSerializer(serializers.ModelSerializer):

    class Meta:
        model = LocationModel
        fields = '__all__'

class StationSerializer(serializers.ModelSerializer):

    class Meta:
        model = StationModel
        fields = '__all__'

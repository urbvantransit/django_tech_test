# coding: utf8
from rest_framework import serializers

from apps.stations.models import LocationModel


class LocationSerializer(serializers.ModelSerializer):

    class Meta:
        model = LocationModel
        exclude = ('id', )

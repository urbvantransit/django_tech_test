# coding: utf8
from rest_framework import serializers

from .. import models


class LocationSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = models.LocationModel
        exclude = []


class StationSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.StationModel
        exclude = []

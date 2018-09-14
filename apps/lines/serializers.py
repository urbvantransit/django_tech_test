# coding: utf8
from rest_framework.serializers import HyperlinkedModelSerializer

from . import models


class LineSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = models.LineModel
        exclude = []


class RouteSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = models.RouteModel
        exclude = []

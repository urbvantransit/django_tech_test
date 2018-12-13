# coding: utf8
from rest_framework import serializers

from ..models import (LineModel, RouteModel)


class LineSerializer(serializers.ModelSerializer):
    """
        REST Framework serializer for the Line Model
    """
    class Meta:
        model = LineModel
        fields = '__all__'


class RouteSerializer(serializers.ModelSerializer):
    """
        REST Framework serializer for the Route Model
    """
    class Meta:
        model = RouteModel
        fields = '__all__'

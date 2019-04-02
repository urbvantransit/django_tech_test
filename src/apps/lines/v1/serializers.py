# coding: utf8
from rest_framework import serializers

from ...lines.models import LineModel, RouteModel


class LineSerializer(serializers.ModelSerializer):

    class Meta:
        model = LineModel
        exclude = ('id', )


class RouteSerializer(serializers.ModelSerializer):

    class Meta:
        model = RouteModel
        exclude = ('id', )
        extra_kwargs = {'stations': {'required': False}}

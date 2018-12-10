# coding: utf8
from rest_framework import serializers

from ..models import (LineModel, RouteModel)


class LineSerializer(serializers.ModelSerializer):

    class Meta:
        model = LineModel
        #exclude = ('id', )
        fields = ('name', 'color', 'routes')


class RouteSerializer(serializers.ModelSerializer):

    class Meta:
        model = RouteModel
        exclude = ('id', )

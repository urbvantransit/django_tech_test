# coding: utf-8
from rest_framework import serializers

from apps.lines.models import LineModel, RouteModel


class LineSerializer(serializers.ModelSerializer):

    class Meta:
        model = LineModel
        exclude = ('id', )


class RouteSerializer(serializers.ModelSerializer):

    class Meta:
        model = RouteModel
        exclude = ('id', )

    def create(self, validated_data):
        stations = validated_data.get('stations')
        validated_data.pop('stations')
        instance = RouteModel.objects.create(**validated_data)

        for station in stations:
            instance.stations.add(station)

        return instance

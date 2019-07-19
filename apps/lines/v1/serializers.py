from rest_framework import serializers

from apps.lines.models import (LineModel, RouteModel)


class LineSerializer(serializers.ModelSerializer):
    class Meta:
        model = LineModel


class RouteSerializer(serializers.ModelSerializer):
    class Meta:
        model = RouteModel
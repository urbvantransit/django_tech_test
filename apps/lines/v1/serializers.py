from rest_framework import serializers
from apps.lines.models import LineModel, RouteModel


class LineModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = LineModel
        fields = ("id", "name", "color")


class RouteModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = RouteModel
        fields = ("line", "stations", 'direction', 'is_active')

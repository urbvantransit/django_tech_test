# THIRD-PARTY IMPORTS
from rest_framework import serializers

# URBVAN IMPORTS
from ..models import (
    LineModel,
    RouteModel,
)


class LineModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = LineModel
        fields = '__all__'


class RouteModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = RouteModel
        fields = '__all__'

# users/serializers.py
from rest_framework import serializers
from .models import LineModel,RouteModel


class LineSerializer(serializers.ModelSerializer):

    class Meta:
        model = LineModel
        exclude = ('id', )

class RouteSerializer(serializers.ModelSerializer):

    class Meta:
        model = RouteModel
        exclude = ('id', )

from rest_framework import serializers

from ..models import LineModel, RouteModel


class LineSerializer(serializers.ModelSerializer):

    class Meta:
        model = LineModel
        exclude = ('id', )


class LineSerializerId(serializers.ModelSerializer):

    class Meta:
        model = LineModel
        exclude = ()


class RouteSerializer(serializers.ModelSerializer):

    class Meta:
        model = RouteModel
        exclude = ('id', )


class RouteSerializerId(serializers.ModelSerializer):

    class Meta:
        model = RouteModel
        exclude = ()

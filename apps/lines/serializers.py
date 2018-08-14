# users/serializers.py
from rest_framework import serializers
from .models import LineModel


class LineSerializer(serializers.ModelSerializer):
    name = serializers.CharField(max_length=200)
    color = serializers.CharField(max_length=200)

    def create(self, validated_data):
        instance = self.Meta.model(**validated_data)
        instance.save()
        return instance

    def update(self, instance, validated_data):
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()
        return instance

    class Meta(object):
        model = LineModel
        fields = ('name', 'color')

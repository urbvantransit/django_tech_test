# users/serializers.py
from rest_framework import serializers
from .models import LineModel


class LineSerializer(serializers.ModelSerializer):

    def create(self, validated_data):
        instance = self.Meta.model(**validated_data)
        instance.save()
        return instance

    # def update(self, instance, validated_data):
    #     for attr, value in validated_data.items():
    #         if attr == 'password':
    #             instance.set_password(value)
    #         else:
    #             setattr(instance, attr, value)
    #     instance.save()
    #     return instance

    class Meta(object):
        model = LineModel
        fields = ('name', 'color')

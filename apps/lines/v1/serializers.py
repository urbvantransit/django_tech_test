from rest_framework import serializers
from apps.lines.models import LineModel


class LineModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = LineModel
        fields = ("id", "name", "color")

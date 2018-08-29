
from rest_framework import serializers

from apps.lines.models import LineModel


class LineSerializer(serializers.ModelSerializer):

    class Meta:
        model = LineModel
        exclude = ('id',)

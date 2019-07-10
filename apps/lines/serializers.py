from rest_framework import serializers

from .models import LineModel

class LineSerializer(serializers.ModelSerializer):
    class Meta:
        model = LineModel
        fields = [
            'id',
            'name',
            'color'
        ]

    def validate(self, data):
        name = data.get("name", None)
        color = data.get("color", None)
        if name == "": # el nombre no debe ser un string vacio
            name = None
        
        if name is None:
            raise serializers.ValidationError("Nombre y color son requeridos.")
        return data
# Se importa serializers, nos permite convertir datos complejos
# en datos nativos de Python y posteriormente, en JSON
from rest_framework import serializers

# Importamos los modelos LineModel y RouteModel desde 
# apps.line.models que es donde se encuentran
from apps.lines.models import LineModel, RouteModel

# creamos una clase `LineSerializer` que hereda de `ModelSerializer`
class LineSerializer(serializers.ModelSerializer):
    """
    Clase que proporciona la información del modelo LineModel
    `id`, `name` y `color`
    """

    class Meta:
        model = LineModel
        fields = '__all__'
        read_only_fields = ('user', )

class RouteModelSerailizer(serializers.ModelSerializer):
    """
    Clase que proporciona la información del modelo 
    `RouteModel` y sus respectivos campos :
        `id`, `line`, `stations`, `direction` & `is_active`
    """
    class Meta:
        model = RouteModel
        fields = '__all__'
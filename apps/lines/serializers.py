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

    #line = LineSerializer(required=False)
    createdAt = serializers.SerializerMethodField()
    updatedAt = serializers.SerializerMethodField()
    url = serializers.SerializerMethodField()

    class Meta:
        model = RouteModel
        fields = ('__all__')
        read_only_fields = ('user', 'line', )

    def get_createdAt(self, obj):
        return obj.createdAt.isoformat()

    def get_updatedAt(self, obj):
        return obj.updatedAt.isoformat()

    def get_url(self, obj):
        return obj.get_absolute_url()

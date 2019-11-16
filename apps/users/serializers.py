from rest_framework import serializers
from rest_framework.validators import UniqueValidator

from .models import User


class UserCreateSerializer(serializers.ModelSerializer):
    """
    Clase que proporciona los datos necesarios para poder crear
    un usuario, estos datos especiales se convierten en formato JSON
    """
    email = serializers.EmailField(required=True, validators = [
        UniqueValidator(queryset=User.objects.all(), message="Ya existe un usuario con este email.")
    ])
    password = serializers.CharField(min_length=8, max_length=12, required=True, write_only=True)

    class Meta:
        model = User
        fields = ('email', 'password', 'is_driver', )

    def create(self, validated_data):
        user = User(email=validated_data['email'])
        user.set_password(validated_data['password'])
        user.save()
        return user

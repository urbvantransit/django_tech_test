from rest_framework import serializers
from ..models import User

 
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username','password','is_tier2', 'is_tier3')
        read_only_fields = ('is_staff', 'is_superuser', 'is_active', 'date_joined',)
        extra_kwargs = {
            'password': {'write_only': True},
        }
 
    def create(self, validated_data):
        user = User.objects.create(**validated_data)
        user.set_password(validated_data['password'])
        user.save()
        return user

    def update(self, instance, validated_data):
        for attr, value in validated_data.items():
            if attr == 'password':
                instance.set_password(value)
            else:
                setattr(instance, attr, value)
        instance.save()
        return instance
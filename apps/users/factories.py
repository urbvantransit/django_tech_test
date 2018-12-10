# coding: utf8
import factory

from rest_framework.authtoken.models import Token

from .models import User


class UserFactory(factory.django.DjangoModelFactory):

    class Meta:
        model = User

    username = factory.Faker('user_name')
    email = factory.Faker('safe_email')
    first_name = factory.Faker('first_name')
    last_name = factory.Faker('last_name')
    is_active = True
    user_type = 3


class TokenFactory(factory.django.DjangoModelFactory):

    class Meta:
        model = Token
        django_get_or_create = ('user',)

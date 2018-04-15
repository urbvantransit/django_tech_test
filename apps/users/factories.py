# coding: utf8
import factory

from django.contrib.auth.models import User

from rest_framework.authtoken.models import Token


class UserFactory(factory.django.DjangoModelFactory):

    class Meta:
        model = User

    username = factory.Faker('user_name')
    email = factory.Faker('safe_email')
    first_name = factory.Faker('first_name')
    last_name = factory.Faker('last_name')
    is_active = True


class TokenFactory(factory.django.DjangoModelFactory):

    class Meta:
        model = Token
        django_get_or_create = ('user',)

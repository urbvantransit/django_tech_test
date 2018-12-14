# coding: utf8
import logging

import factory
from django.contrib.auth.models import User, Group, Permission
from rest_framework.authtoken.models import Token

from apps.users.management.commands.create_users_and_groups import MODELS, GROUPS_AND_PERMISSIONS


class UserFactory(factory.django.DjangoModelFactory):

    class Meta:
        model = User

    username = factory.Faker('user_name')
    email = factory.Faker('safe_email')
    first_name = factory.Faker('first_name')
    last_name = factory.Faker('last_name')
    is_active = True

class PermissionFactory(factory.django.DjangoModelFactory):

    class Meta:
        model = Permission

class AdminGroupFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Group

    name = "Admins"

    @factory.post_generation
    def permissions(self, create, extracted, **kwargs):
        for obj in GROUPS_AND_PERMISSIONS:
            if obj['name'] == self.name:
                for model in MODELS:
                    for name in obj.get('permissions'):
                        permission_name = 'Can {} {}'.format(name, model)
                        try:
                            model_permission = Permission.objects.get(name=permission_name)
                            self.permissions.add(model_permission)
                        except Permission.DoesNotExist:
                            logging.warning('Permission not found: {}'.format(permission_name))


class AdminUserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = User

    username = "admin"
    first_name = "admin"
    group = factory.SubFactory(AdminGroupFactory,)
    password = "admin_test"
    is_active = True


class TokenFactory(factory.django.DjangoModelFactory):

    class Meta:
        model = Token
        django_get_or_create = ('user',)

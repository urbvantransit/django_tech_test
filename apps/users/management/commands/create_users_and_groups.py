# created by victor p - 12/12/2018 -
# Create all groups required by the application and a user by group
# coding: utf8

from django.core.management.base import BaseCommand
from django.contrib.auth.models import (Group, Permission, User)
import logging

GROUPS_AND_PERMISSIONS = [
    {'name': 'Admins',
     'permissions': ['view', 'add', 'change', 'delete'],
     'users': ['admin']},
    {'name': 'Editors',
     'permissions': ['view', 'add', 'change'],
     'users': ['editor']},
    {'name': 'Users',
     'permissions': ['view'],
     'users': ['user']},
]
MODELS = ['location model', 'station model', 'route model', 'line model']


class Command(BaseCommand):
    help = 'Create the base groups, users, and permissions for the api models'

    def handle(self, *args, **options):
        for obj in GROUPS_AND_PERMISSIONS:
            group, created = Group.objects.get_or_create(name=obj.get('name'))
            for username in obj.get('users'):
                user, created = User.objects.get_or_create(username=username,
                                                           defaults={'first_name': username,
                                                                     'password': 'test_{}'.format(username)})
                if created:
                    group.user_set.add(user)
                    user.set_password('test_{}'.format(username))
                    user.save()

            for model in MODELS:
                for name in obj.get('permissions'):
                    permission_name = 'Can {} {}'.format(name, model)
                    try:
                        model_permission = Permission.objects.get(name=permission_name)
                        group.permissions.add(model_permission)
                    except Permission.DoesNotExist:
                        logging.warning('Permission not found: {}'.format(permission_name))

        print("Groups and permissions created.")

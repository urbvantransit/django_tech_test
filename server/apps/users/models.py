# coding: utf-8

from django.conf import settings
from django.db import models


class Permission(models.Model):
    ADMIN = 'A'
    DRIVER = 'D'
    USER = 'U'

    PERMISSION_TYPE = (
        (ADMIN, u"Administrador"),
        (DRIVER, u"Conductor"),
        (USER, u"Usuario"),
    )

    option = models.CharField(
        max_length=1,
        choices=PERMISSION_TYPE,
        default=READ
    )

    def __str__(self):
        return self.get_option_display()


class UserPermission(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        primary_key=True,
        related_name='permissions'
    )
    permission = models.ForeignKey(Permission)

    def __str__(self):
        return self.permission.option
# coding: utf8

from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext as _

class User(AbstractUser):
    """
    Custom User Model for Urbvan
    """
    #: Types of Users available
    USER_TYPE_SUPERVISOR = 1
    USER_TYPE_DRIVER = 2
    USER_TYPE_PASSENGER = 3
    USER_TYPE_CHOICES = (
        (USER_TYPE_SUPERVISOR, _("Supervisor")),
        (USER_TYPE_DRIVER, _("Driver")),
        (USER_TYPE_PASSENGER, _("Passenger"))
    )

    user_type = models.PositiveSmallIntegerField(
        choices=USER_TYPE_CHOICES, default=USER_TYPE_PASSENGER
    )

    class Meta:
        db_table = "auth_user"

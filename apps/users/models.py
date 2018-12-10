# coding: utf8

from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext as _

from .user_types import (USER_TYPES, get_user_type_choices)



class User(AbstractUser):
    """
    Custom User Model for Urbvan
    """
    
    user_type = models.PositiveSmallIntegerField(
        choices=get_user_type_choices(), default=USER_TYPES["passenger"]
    )
    
    class Meta:
        db_table = "auth_user"

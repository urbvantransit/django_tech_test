# coding: utf8
from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    """ User class with added permision 

        Fields:
            is_tier2 -- gives user IsAuthenticated and IsTier2 permisions (boolean)
            is_tier3 -- gives user logged in, Tier2Uaer
    """
    is_tier2 = models.BooleanField(default=False)
    is_tier3 = models.BooleanField(default=False)

    def __str__(self):
        return self.username

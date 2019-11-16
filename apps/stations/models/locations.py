# coding: utf8
from django.conf import settings
from django.db import models

from apps.core.models import TimeStampedModel
from apps.utils import create_id


class LocationModel(TimeStampedModel):
    """ Location object is the representation of physical station

        Fields:
            id -- This is the unique identifier for object instance.
            user -- Is the user who create the Location.
            name -- This is the common identifier for a physical location.
            coordinates --  Latitude and Longuitude as string.
                            example. "19.4094937,-99.1634261"
            geometry -- Similar to coordinate but using with postgis
    """

    id = models.CharField(default=create_id('loc_'), primary_key=True,
                          max_length=30, unique=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='user_loc', on_delete=models.DO_NOTHING)
    name = models.CharField(max_length=100)
    latitude = models.DecimalField(max_digits=19, decimal_places=16)
    longitude = models.DecimalField(max_digits=19, decimal_places=16)

    def __str__(self):
        return self.name

# coding: utf8
#DJANGO CORE IMPORTS
from django.db import models

# URBVAN IMPORTS
from apps.utils import create_id


class LocationModel(models.Model):
    """ Location object is the representation of physical station

        Fields:
            id -- This is the unique identifier for object instance.
            name -- This is the common identifier for a physical location.
            coordinates --  Latitude and Longuitude as string.
                            example. "19.4094937,-99.1634261"
            geometry -- Similar to coordinate but using with postgis
    """

    id = models.CharField(
        default=create_id('loc_'),
        primary_key=True,
        max_length=30,
        unique=True
    )
    name = models.CharField(max_length=100)
    latitude = models.DecimalField(max_digits=19, decimal_places=16)
    longitude = models.DecimalField(max_digits=19, decimal_places=16)

    @property
    def coordinates(self):
        return '{},{}'.format(self.latitude, self.longitude)

    def geometry(self):
        # TODO
        pass

    def __str__(self):
        return self.name

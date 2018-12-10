# coding: utf8
from functools import partial

from django.db import models

from apps.utils import create_id
from apps.users.user_types import USER_TYPES as UT


def create_id_for_LocationModel():
    """
    Helper function for creating ids for the Location Model
    """
    return create_id('loc_')


class LocationModel(models.Model):
    """ Location object is the representation of physical station

        Fields:
            id -- This is the unique identifier for object instance.
            name -- This is the common identifier for a physical location.
            latitude -- Latitude of the location - decimal, i.e. -99.1634261
            longitude -- Longitude of the location - decimal, i.e. -99.1634261
    """
    MODEL_CRUD_PERMISSIONS = {
        "create": [ UT["supervisor"], UT["driver"] ], 
        "retrieve": [ UT["supervisor"], UT["driver"], UT["passenger"] ], 
        "update": [ UT["supervisor"], UT["driver"] ], 
        "delete": [ UT["supervisor"], UT["driver"] ], 
    }

    id = models.CharField(default=create_id_for_LocationModel, primary_key=True,
                          max_length=30, unique=True)
    name = models.CharField(max_length=100)
    latitude = models.DecimalField(max_digits=19, decimal_places=16)
    longitude = models.DecimalField(max_digits=19, decimal_places=16)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['-id', ]

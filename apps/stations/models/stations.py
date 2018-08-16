# coding: utf8
from django.db import models

from .locations import LocationModel

from apps.utils import create_id


class StationModel(models.Model):
    """
    StationModel class is child of django.db model and 
    is the represetation of a station in a route related to 
    :model:`stations.LocationModel`.
    Fields:
            id -- This is the unique identifier for object instance.
            location -- This is related to :model:`stations.LocationModel`
            order -- this is for enum the stations in a route
            is_active -- boolean for logic erasing
    """

    id = models.CharField(default=create_id('sta_'), primary_key=True,
                          max_length=30, unique=True)
    location = models.ForeignKey(LocationModel, on_delete=models.DO_NOTHING)
    order = models.IntegerField(default=0)
    is_active = models.BooleanField(default=True)
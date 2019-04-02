# coding: utf8
from django.db import models

from .locations import LocationModel
from ...utils import create_id


def create_station_id():
    """
    Function for create ID for station model
    """
    return create_id('sta_')


class StationModel(models.Model):
    id = models.CharField(
        default=create_station_id,
        primary_key=True,
        max_length=30,
        unique=True
    )
    order = models.IntegerField(default=0)
    is_active = models.BooleanField(default=True)

    # Relationships
    location = models.ForeignKey(LocationModel, on_delete=models.DO_NOTHING)
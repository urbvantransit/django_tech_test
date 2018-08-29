# coding: utf8
from django.db import models

from .locations import LocationModel

from apps.utils import create_station_id


class StationModel(models.Model):

    id = models.CharField(default=create_station_id, primary_key=True,
                          max_length=30, unique=True)
    location = models.ForeignKey(LocationModel, on_delete=models.DO_NOTHING)
    order = models.IntegerField(default=0)
    is_active = models.BooleanField(default=True)

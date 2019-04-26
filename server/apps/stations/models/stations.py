# coding: utf-8
from django.db import models

from apps.stations.models.locations import LocationModel

from apps.utils import create_id


def create_station_id():
    return create_id('sta_id')


class StationModel(models.Model):

    class Meta:
        ordering = ['-id']

    id = models.CharField(default=create_station_id, primary_key=True,
                          max_length=30, unique=True)
    location = models.ForeignKey(
        LocationModel, on_delete=models.DO_NOTHING, related_name='stations')
    order = models.IntegerField(default=0)
    is_active = models.BooleanField(default=True)

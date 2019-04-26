# coding: utf-8
from django.db import models

from apps.lines.models import LineModel
from apps.stations.models import StationModel

from apps.utils import create_id


def create_route_id():
    return create_id('route_')


class RouteModel(models.Model):

    class Meta:
        ordering = ['-id']

    id = models.CharField(default=create_route_id, primary_key=True,
                          max_length=30, unique=True)
    line = models.ForeignKey(LineModel, on_delete=models.DO_NOTHING)
    stations = models.ManyToManyField(StationModel)
    direction = models.BooleanField(default=True)
    is_active = models.BooleanField(default=True)

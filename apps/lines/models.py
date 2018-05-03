# coding: utf8

from django.db import models
from apps.stations.models import StationModel
from apps.utils import create_id
from colorful.fields import RGBColorField


class LineModel(models.Model):

    id = models.CharField(default=create_id('line_'), primary_key=True,
                          max_length=30, unique=True)
    name = models.CharField(max_length=100)
    color = RGBColorField()

    def __str__(self):
        return self.name


class RouteModel(models.Model):

    id = models.CharField(default=create_id('route_'), primary_key=True,
                          max_length=30, unique=True)
    line = models.ForeignKey(LineModel, on_delete=models.DO_NOTHING)
    stations = models.ManyToManyField(StationModel)
    direction = models.BooleanField(default=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.id

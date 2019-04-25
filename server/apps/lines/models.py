# coding: utf-8
from django.db import models

from apps.stations.models import StationModel

from apps.utils import create_id


def create_line_id():
    return create_id('line_')


def create_route_id():
    return create_id('route_')


class LineModel(models.Model):

    id = models.CharField(default=create_line_id, primary_key=True,
                          max_length=30, unique=True)
    name = models.CharField(max_length=100)
    color = models.CharField(max_length=8)


class RouteModel(models.Model):

    id = models.CharField(default=create_route_id, primary_key=True,
                          max_length=30, unique=True)
    line = models.ForeignKey(LineModel, on_delete=models.DO_NOTHING)
    stations = models.ManyToManyField(StationModel)
    direction = models.BooleanField(default=True)
    is_active = models.BooleanField(default=True)

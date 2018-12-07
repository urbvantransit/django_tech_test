# coding: utf8
from django.db import models

from apps.stations.models import StationModel

from apps.utils import create_id


def create_id_for_LineModel():
    """
    Helper function for creating ids for the Line Model
    """
    return create_id('line_')


class LineModel(models.Model):

    id = models.CharField(default=create_id_for_LineModel, primary_key=True,
                          max_length=30, unique=True)
    name = models.CharField(max_length=100)
    color = models.CharField(max_length=8)


def create_id_for_RouteModel():
    """
    Helper function for creating ids for Route Model
    """
    return create_id('route_')


class RouteModel(models.Model):

    id = models.CharField(default=create_id_for_RouteModel, primary_key=True,
                          max_length=30, unique=True)
    line = models.ForeignKey(LineModel, on_delete=models.DO_NOTHING)
    stations = models.ManyToManyField(StationModel)
    direction = models.BooleanField(default=True)
    is_active = models.BooleanField(default=True)

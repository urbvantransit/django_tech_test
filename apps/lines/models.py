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
    """ Line object is the representation of a line (a group of routes).

        Fields:
            id -- This is the unique identifier for object instance.
            name -- This is the common identifier for a line.
            color --  The color of the line
    """

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
    """ Line object is the representation of a route.

        Fields:
            id -- This is the unique identifier for object instance.
            line -- This is the line the route belongs.
            stations --  The stations that route goes through.
            direction -- The direction of the route (True if forward?)
            is_active - If the route is active
    """

    id = models.CharField(default=create_id_for_RouteModel, primary_key=True,
                          max_length=30, unique=True)
    line = models.ForeignKey(LineModel, on_delete=models.DO_NOTHING)
    stations = models.ManyToManyField(StationModel)
    direction = models.BooleanField(default=True)
    is_active = models.BooleanField(default=True)

# coding: utf8
from django.db import models

from apps.stations.models import StationModel

from apps.utils import create_id


class LineModel(models.Model):
    """ Line
        Fields:
            id -- This is the unique identifier for object instance.
            name -- This is the common identifier for a line.
            color --  Color for line object instance.
    """

    id = models.CharField(default=create_id('line_'), primary_key=True,
                          max_length=30, unique=True)
    name = models.CharField(max_length=100)
    color = models.CharField(max_length=8)


class RouteModel(models.Model):
    """ Route
        Fields:
            id -- This is the unique identifier for object instance.
            line -- Reference of unique identifier of line instance.
            stations --  Reference of unique identifier of station instance
            direction -- Shows direction of the route.
            is_active -- Shows if route is active.
    """
    id = models.CharField(default=create_id('route_'), primary_key=True,
                          max_length=30, unique=True)
    line = models.ForeignKey(LineModel, on_delete=models.DO_NOTHING)
    stations = models.ManyToManyField(StationModel)
    direction = models.BooleanField(default=True)
    is_active = models.BooleanField(default=True)

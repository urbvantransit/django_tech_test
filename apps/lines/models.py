# coding: utf8
from django.db import models

from apps.stations.models import StationModel

from apps.utils import create_id
"""
This module is for declare LineModel and RouteModel,
this classes are django.db models and are important for
business.
"""

class LineModel(models.Model):
    """
    LineModel class is child of django.db model and
    store a single Line.
    """
    id = models.CharField(default=create_id('line_'), primary_key=True,
                          max_length=30, unique=True)
    name = models.CharField(max_length=100)
    color = models.CharField(max_length=8)


class RouteModel(models.Model):
    """
    RouteModel class is child of django.db model and 
    store a single Route related to :model:`lines.LineModel`
    """
    id = models.CharField(default=create_id('route_'), primary_key=True,
                          max_length=30, unique=True)
    line = models.ForeignKey(LineModel, on_delete=models.DO_NOTHING)
    stations = models.ManyToManyField(StationModel)
    direction = models.BooleanField(default=True)
    is_active = models.BooleanField(default=True)

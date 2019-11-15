# coding: utf8
from django.db import models
from apps.stations.models import StationModel
from apps.utils import create_id
from django.db.models.signals import pre_save


class LineModel(models.Model):

    id = models.CharField(
        default=create_id("line_"), primary_key=True, max_length=30, unique=True
    )
    name = models.CharField(max_length=100)
    color = models.CharField(max_length=8)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-id"]


class RouteModel(models.Model):

    id = models.CharField(
        default=create_id("route_"), primary_key=True, max_length=30, unique=True
    )
    line = models.ForeignKey(LineModel, on_delete=models.DO_NOTHING)
    stations = models.ManyToManyField(StationModel)
    direction = models.BooleanField(default=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-id"]


"""
Add pre_save to generate id for RouteModel and LineModel
"""


def pre_route_create_id(sender, instance, **kwargs):
    instance.id = create_id("route_")


def pre_line_create_id(sender, instance, **kwargs):
    instance.id = create_id("line_")


pre_save.connect(pre_route_create_id, sender=RouteModel)
pre_save.connect(pre_line_create_id, sender=LineModel)

# coding: utf8
# created by victor p - 12/12/2018 - Refactoring apps/lines/models.py

from django.db import models
from apps.utils import create_id
from .lines import LineModel
from apps.stations.models import LocationModel

class RouteModel(models.Model):
    """
        RouteModel: Django model for a Route of a line
    """
    class Meta:
        ordering = ['id']
        verbose_name = 'route'
        verbose_name_plural = 'routes'

    id = models.CharField(default=create_id('route_'), primary_key=True,
                          max_length=30, unique=True)
    line = models.ForeignKey(LineModel, on_delete=models.DO_NOTHING)
    stations = models.ManyToManyField(LocationModel, through="stations.StationModel", blank=True)
    direction = models.BooleanField(default=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return ('Route {} - {}'.format(self.line,self.direction))
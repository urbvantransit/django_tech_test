# coding: utf8
from django.db import models

from apps.utils import create_id
from .locations import LocationModel


class StationModel(models.Model):
    class Meta:
        ordering = ('id',)

    id = models.CharField(default=create_id('sta_'), primary_key=True,
                          max_length=30, unique=True)
    location = models.ForeignKey(LocationModel, on_delete=models.DO_NOTHING)
    order = models.IntegerField(default=0)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f'{self.order} @ {self.location} '

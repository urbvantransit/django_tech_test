# coding: utf8
from django.db import models

from .locations import LocationModel

from apps.utils import create_id


class StationModel(models.Model):

    id = models.CharField(default=create_id('sta_'), primary_key=True,
                          max_length=30, unique=True)
    location = models.ForeignKey(LocationModel, on_delete=models.DO_NOTHING)
    order = models.IntegerField(default=0)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.id

# coding: utf8
from django.db import models

from .locations import LocationModel

from apps.utils import create_id


class StationModel(models.Model):

    id = models.AutoField(auto_created=True, primary_key=True,
                          max_length=30, unique=True)
    name = models.CharField(max_length=100)
    location = models.ForeignKey(LocationModel, on_delete=models.DO_NOTHING)
    order = models.IntegerField(default=0)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name

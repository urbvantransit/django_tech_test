# coding: utf8
from django.db import models

from .locations import LocationModel

from apps.utils import create_id


def create_id_for_StationModel():
	"""
    Helper function for creating ids for the Station Model
    """
	return create_id('sta_')


class StationModel(models.Model):

    id = models.CharField(default=create_id_for_StationModel, primary_key=True,
                          max_length=30, unique=True)
    location = models.ForeignKey(LocationModel, on_delete=models.DO_NOTHING)
    order = models.IntegerField(default=0)
    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ['-id', ]

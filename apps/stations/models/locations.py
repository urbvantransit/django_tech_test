# coding: utf8
from django.db import models

from apps.utils import create_id


class LocationModel(models.Model):
    """ Location object is the representation of physical station

        Fields:
            id -- This is the unique identifier for object instance.
            name -- This is the common identifier for a physical location.
            latitude -- latitude coordinate as decimal
            longitude -- longitude coordinate as decimal
    """
    class Meta:
        ordering = ['id']
        verbose_name = 'location'
        verbose_name_plural = 'locations'

    id = models.CharField(default=create_id('loc_'), primary_key=True,
                          max_length=30, unique=True)
    name = models.CharField(max_length=100)
    latitude = models.DecimalField(max_digits=19, decimal_places=16)
    longitude = models.DecimalField(max_digits=19, decimal_places=16)

    def __str__(self):
        return self.name

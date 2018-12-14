# coding: utf8
# created by victor p - 12/12/2018 - Refactoring apps/lines/models.py

from django.db import models
from apps.utils import create_id


class LineModel(models.Model):
    """
        LineModel: Django model for a Urbvan line
    """
    class Meta:
        ordering = ['id']
        verbose_name = 'line'
        verbose_name_plural = 'lines'

    id = models.CharField(default=create_id('line_'), primary_key=True,
                          max_length=30, unique=True)
    name = models.CharField(max_length=100)
    color = models.CharField(max_length=8)

    def __str__(self):
        return self.name

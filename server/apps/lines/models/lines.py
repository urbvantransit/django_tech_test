# coding: utf-8
from django.db import models

from apps.utils import create_id


def create_line_id():
    return create_id('line_')


class LineModel(models.Model):

    class Meta:
        ordering = ['-id']

    id = models.CharField(default=create_line_id, primary_key=True,
                          max_length=30, unique=True)
    name = models.CharField(max_length=100)
    color = models.CharField(max_length=8)

    def __str__(self):
        return self.name

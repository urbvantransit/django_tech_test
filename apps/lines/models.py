# coding: utf8
from django.db import models
from django.conf import settings
from django.urls import reverse

from apps.stations.models import StationModel
from apps.utils import create_id
from apps.core.models import TimeStampedModel


# ********* IMPORTANTE ********* #
# Se agrega TimeStampedModel a `LineModel` & `RouteModel`
# para tener un mayor control sobre ellos, y más info

class LineModel(TimeStampedModel):

    id = models.CharField(default=create_id('line_'), primary_key=True,
                          max_length=30, unique=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='user_line', on_delete=models.DO_NOTHING)
    name = models.CharField(max_length=100)
    color = models.CharField(max_length=8)

    def __str__(self):
        return self.id

    def get_absolute_url(self):
        return reverse("lines_routes:lines_detail", kwargs={"id": self.id})
    
class RouteModel(TimeStampedModel):

    id = models.CharField(default=create_id('route_'), primary_key=True,
                          max_length=30, unique=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='user_route' ,on_delete=models.DO_NOTHING)
    line = models.ForeignKey(LineModel, related_name='routes', on_delete=models.DO_NOTHING)
    stations = models.ManyToManyField(StationModel)
    direction = models.BooleanField(default=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f"Ruta - {self.id} linea - {self.line.name}"

    def get_absolute_url(self):
        return reverse("lines_routes:routes_detail", kwargs={"id": self.id})

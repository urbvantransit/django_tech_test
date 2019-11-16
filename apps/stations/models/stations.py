# coding: utf8
from django.conf import settings
from django.db import models

from apps.core.models import TimeStampedModel
from apps.utils import create_id

from .locations import LocationModel


class StationModel(TimeStampedModel):
    """ Station, es un objecto que representa una estación en
    una determinana localización

        id -- Identificador único del objeto.
        user -- El usuario que creó el objeto.
        location -- la localización (zona geográfica) en la que se 
                    encuentra la estación
        order -- No sé a que se refiere
        is_active -- Un valor True o False que determina si la estación
                    Está activa o no

    """

    id = models.CharField(default=create_id('sta_'), primary_key=True,
                          max_length=30, unique=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='user_station', on_delete=models.DO_NOTHING)
    location = models.ForeignKey(LocationModel, on_delete=models.DO_NOTHING)
    order = models.IntegerField(default=0)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f"Estación {self.id} en {self.location.name}"

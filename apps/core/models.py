from django.db import models


class TimeStampedModel(models.Model):
    """
    Un modelo clase que nos provee de un campo
    `createdAt` & `updatedAt` en cualquier modelo hijo
    del cual herede éste.
    """
    createdAt = models.DateTimeField('Fecha de Creación', auto_now_add=True, null=True)
    updatedAt = models.DateTimeField('Fecha de Actualización', auto_now=True, null=True)

    class Meta:
        abstract = True
        ordering = ('-createdAt', )

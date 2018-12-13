# coding: utf8
# created by victor p - 13/12/2018 -
# Lines app business rules

from django.db.models.signals import pre_save
from django.dispatch import receiver

from .routes import RouteModel


@receiver(pre_save, sender=RouteModel)
def pre_save_routes(sender,**kwargs):
    """
    :param sender: The sender class
    :param kwargs: parameter collection containing the saved instance
    :return: None
    Check if the line has already an active route
    """
    # line = models.ForeignKey(LineModel, on_delete=models.DO_NOTHING)
    # stations = models.ManyToManyField(StationModel)
    # direction = models.BooleanField(default=True)
    # is_active = models.BooleanField(default=True)

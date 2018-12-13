# coding: utf8
# created by victor p - 13/12/2018 -
# Lines app business rules

from django.db.models.signals import pre_save
from django.dispatch import receiver
from .exceptions import DuplicatedActiveStationException
from .stations import StationModel


@receiver(pre_save, sender=StationModel)
def pre_save_station(sender,**kwargs):
    """
    :param sender: The sender class
    :param kwargs: parameter collection containing the saved instance
    :return: None
    Check if the station is already included in a route
    """
    instance = kwargs.get('instance')
    if instance.is_active and instance.route.stationmodel_set.filter(location_id=instance.location_id,
                                                    is_active=True)\
            .exclude(id=instance.id).exists():

        raise DuplicatedActiveStationException()
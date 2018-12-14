# coding: utf8
# created by victor p - 13/12/2018 -
# Lines app business rules

from django.db.models.signals import pre_save
from django.dispatch import receiver
from .exceptions import MultipleActiveRouteException
from .routes import RouteModel


@receiver(pre_save, sender=RouteModel)
def pre_save_route(sender, **kwargs):
    """
    Check if the line has already an active route
    :param sender: The sender class
    :param kwargs: parameter collection containing the saved instance
    :return: None
    """
    instance = kwargs.get('instance')
    if instance.is_active and RouteModel.objects.filter(line_id=instance.line_id,
                                                        is_active=True)\
                                                .exclude(id=instance.id or -1).exists():

        raise MultipleActiveRouteException()

from django.contrib.auth.models import Group
from django.db.models.signals import post_save
from django.dispatch import receiver

from .models import DriveProfile, UserProfile
from .models import User


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    """
    Función que nos permite guardar los perfiles de los usuarios
    después de su creación con `post_save`, revisa si, el usuario
    al momento de su creación tiene `is_driver=True`, de ser verdadero
    crea un perfil de `driver`, de lo contrario crea un perfil normal
    """
    if created:
        if instance.is_driver:
            DriveProfile.objects.create(user=instance)
            #group = Group.objects.get(name='drivers')
            #instance.groups.add(Group)
            instance.driverprofile.save()
        else:
            UserProfile.objects.create(user=instance)
            #group = Group.objects.get(name='clients')
            #instance.groups.add(Group)
            instance.userprofile.save()

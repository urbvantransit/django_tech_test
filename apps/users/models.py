from django.conf import settings
from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.db import models
# modulo para poder traducir el texto a diferentes idiomas
# en caso de ser requerido
from django.utils.translation import ugettext_lazy as _

from apps.core.models import TimeStampedModel

from .managers import UserManager

# ******** IMPORTANTE ************* #
# Se tendrán 3 tipos de usuarios diferentes:
# 1. Administrador (El cual se tendrá como superuser en esta ocasión)
# 2.- Driver/conductor (Con perfil y datos específicos)
# 3.- Usuario normal (un usuario/pasajero con datos del mismo)

class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(_('email address'), unique=True)
    first_name = models.CharField(_('first name'), max_length=30, blank=True)
    last_name = models.CharField(_('last name'), max_length=30, blank=True)
    date_joined = models.DateTimeField(_('date joined'), auto_now_add=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(_('active'), default=True)
    # Existen dos formas de que `is_driver` se vuelva `True`, con un checkbox
    # desde el frontend, o que el administrador lo haga.
    # Al ser True a la hora de registrarse desde el frontend, 
    # se creará un perfil específico para el conductor
    is_driver = models.BooleanField(_("Is driver?"), default=False)

    objects = UserManager()

    class Meta:
        verbose_name = _('User')
        verbose_name_plural = _('Users')

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def get_full_name(self):
        """
        Regresa el nombre + apellidos
        `first_name` + `last_name`
        con un espacio en medio
        """
        return f"{self.first_name} {self.last_name}"

    def get_short_name(self):
        """
        Regresa el primer nombre del usuario `first_name`
        """
        return self.first_name

# Se crearan dos perfiles para tener 3 tipos de usuario
# 1.- Administrador (el cual no necesita de un perfil)
# 2.- Conductor - el cual tendrá campos especiales
# 3.- Usuario - el usuario normal o pasajero
# Heredamos de la clase `TimeStampedModel` para evitar
# tener que repetir código con `createdAt`, etc..
class DriveProfile(TimeStampedModel):
    """
    Una clase modelo que tiene los datos de un chofer de Urbvan
    los cuales no conozco, pero los inventaré, aunque sean pocos
    """
    user = models.OneToOneField(settings.AUTH_USER_MODEL, related_name='driver_p', on_delete=models.CASCADE)
    unidad = models.CharField(_('Number of the transport unit'), max_length=50, blank=True, null=True)
    placas = models.CharField(_('Placas'), max_length=50, blank=True, null=True)

    def __str__(self):
        return self.get_full_name()


class UserProfile(TimeStampedModel):
    """
    Una clase modelo que contiene los datos de un usuario normal
    o pasajero de Urbvan, datos que tampoco se pero inventaré 
    algunos pocos a modo de prueba para después, utilizar en los
    permisos
    """
    user = models.OneToOneField(settings.AUTH_USER_MODEL, related_name='user_p', on_delete=models.CASCADE)
    address = models.CharField(_("Address"), max_length=120, blank=True, null=True)
    location = models.CharField(_("Location"), max_length=50, blank=True)
    # y más datos

    def __str__(self):
        return self.get_full_name()

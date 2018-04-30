from django.db import models
from django.contrib.auth.models import User
from django.core.validators import RegexValidator


REGEX_ONLY_LETTERS = '^[a-zA-Z ]+$'
ONLY_LETTERS_MESSAGE = 'Solo se permiten caracteres en este campo'


class UserCreate(models.Model):
    """Creator."""

    user_create = models.ForeignKey(User, help_text='Usuario que crea el registro', on_delete=models.PROTECT)

    class Meta:
        abstract = True


class TimeStamp(models.Model):
    """Basic data."""

    created = models.DateTimeField(auto_now_add=True, null=True, help_text="Fecha de creacion")
    modified = models.DateTimeField(auto_now=True, null=True, help_text="Fecha de modificacion")

    class Meta:
        abstract = True


class Active(models.Model):
    """Status of the record"""

    active = models.BooleanField(default=True)

    class Meta:
        abstract = True


class Person(models.Model):
    """Person Basic data."""

    first_name = models.CharField(max_length=50, help_text="Nombre de la persona",
                validators=[
                    RegexValidator(
                            regex = REGEX_ONLY_LETTERS,
                            message = ONLY_LETTERS_MESSAGE
                        )
                
                ])
    last_name = models.CharField(max_length=50, help_text="Apellido de la persona",
                validators=[
                    RegexValidator(
                            regex = REGEX_ONLY_LETTERS,
                            message = ONLY_LETTERS_MESSAGE
                        )
                
                ])
    email = models.EmailField(help_text="Email de la persona")


    class Meta:
        abstract = True



# coding: utf8
from django.db import models
from django.core.validators import RegexValidator
from apps.utils import create_id
from apps.help.models import UserCreate, TimeStamp, Active, REGEX_ONLY_LETTERS, ONLY_LETTERS_MESSAGE


class LocationModel(UserCreate, TimeStamp, Active):
    """ Location object is the representation of physical station

        Fields:
            id -- This is the unique identifier for object instance.
            name -- This is the common identifier for a physical location.
            coordinates --  Latitude and Longuitude as string.
                            example. "19.4094937,-99.1634261"
            geometry -- Similar to coordinate but using with postgis
    """

    id = models.CharField(default=create_id('loc_'), primary_key=True,
                          max_length=30, unique=True)
    name = models.CharField(max_length=100,
                     validators=[
                        RegexValidator(
                                regex = REGEX_ONLY_LETTERS,
                                message = ONLY_LETTERS_MESSAGE
                                )
                            ])
    latitude = models.DecimalField(max_digits=19, decimal_places=16)
    longitude = models.DecimalField(max_digits=19, decimal_places=16)
    key = models.CharField(max_length=4, unique=True, help_text="The 3 fisrt letters") 

    def __str__(self):
        return '%s-%s - longitude:%s - latitude:%s' %(self.name, self.key, self.longitude, self.latitude)

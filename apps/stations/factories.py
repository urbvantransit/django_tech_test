# coding: utf8
import factory

from .models import LocationModel


class LocationFactory(factory.django.DjangoModelFactory):

    class Meta:
        model = LocationModel

    name = factory.Faker('slug')
    latitude = factory.Faker('latitude')
    longitude = factory.Faker('longitude')

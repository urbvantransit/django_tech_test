# coding: utf8
import factory

from . import models


class LocationFactory(factory.django.DjangoModelFactory):

    class Meta:
        model = models.LocationModel

    name = factory.Faker('slug')
    latitude = factory.Faker('latitude')
    longitude = factory.Faker('longitude')

class StationFactory(factory.django.DjangoModelFactory):

    class Meta:
        model = models.StationModel

    location = factory.SubFactory(LocationFactory)
    order = 1

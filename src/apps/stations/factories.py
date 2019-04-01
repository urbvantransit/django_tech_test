# coding: utf8
import factory

from .models import LocationModel, StationModel


class LocationFactory(factory.django.DjangoModelFactory):
    name = factory.Faker('slug')
    latitude = factory.Faker('latitude')
    longitude = factory.Faker('longitude')

    class Meta:
        model = LocationModel


class StationFactory(factory.django.DjangoModelFactory):
    order = factory.Faker(1)
    is_active = factory.Faker(True)
    location = factory.SubFactory(LocationFactory)

    class Meta:
        model = StationModel

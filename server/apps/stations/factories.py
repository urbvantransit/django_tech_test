# coding: utf-8
from factory import Faker, SubFactory
from factory.django import DjangoModelFactory

from .models import LocationModel, StationModel


class LocationFactory(DjangoModelFactory):

    class Meta:
        model = LocationModel

    name = Faker('slug')
    latitude = Faker('latitude')
    longitude = Faker('longitude')


class StationFactory(DjangoModelFactory):

    class Meta:
        model = StationModel

    location = SubFactory(LocationFactory)
    order = Faker('random_int')
    is_active = Faker('boolean')

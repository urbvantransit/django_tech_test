# coding: utf8
import factory
from .models import (LocationModel, StationModel, create_id)


class LocationFactory(factory.django.DjangoModelFactory):

    class Meta:
        model = LocationModel

    id = create_id('loc_')
    name = factory.Faker('slug')
    latitude = factory.Faker('latitude')
    longitude = factory.Faker('longitude')

class DummyLocationFactory(factory.django.DjangoModelFactory):

    class Meta:
        model = LocationModel

    name = 'Dummy Location'
    latitude = 0.0
    longitude = 0.0

class StationFactory(factory.django.DjangoModelFactory):

    class Meta:
        model = StationModel

    location = factory.SubFactory(LocationFactory)
    route = factory.SubFactory('apps.lines.factories.RouteFactory')
    order = 0
    is_active = True

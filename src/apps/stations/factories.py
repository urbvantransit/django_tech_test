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
    order = factory.Sequence(lambda n: '%02d' % n)
    is_active = factory.Faker('boolean')
    location = factory.SubFactory(LocationFactory)

    class Meta:
        model = StationModel

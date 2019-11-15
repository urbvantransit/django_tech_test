# coding: utf8
import factory
from faker import Factory
from .models import LocationModel, StationModel

faker = Factory.create()


class LocationFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = LocationModel

    name = factory.Faker("slug")
    # latitude = factory.Faker("longitude")
    # longitude = factory.Faker("longitude")
    coordinates = str(factory.Faker("longitude")) + ", " + str(factory.Faker("longitude"))


class StationFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = StationModel

    location = factory.SubFactory(LocationFactory)
    order = faker.random_number()
    is_active = True

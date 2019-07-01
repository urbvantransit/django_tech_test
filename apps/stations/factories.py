import factory

from .models import LocationModel


class LocationFactory(factory.django.DjangoModelFactory):

    class Meta:
        model = LocationModel

    id = factory.Faker('uuid4')
    name = factory.Faker('slug')
    latitude = factory.Faker('latitude')
    longitude = factory.Faker('longitude')

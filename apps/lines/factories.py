# coding: utf8
import factory

from .models import LineModel, RouteModel
from apps.stations.factories import StationFactory


class LineFactory(factory.django.DjangoModelFactory):

    class Meta:
        model = LineModel

    name = factory.Faker('slug')
    color = factory.Faker('slug')


class RouteFactory(factory.django.DjangoModelFactory):

    class Meta:
        model = RouteModel

    line = factory.SubFactory(LineFactory)
    direction = factory.Faker('boolean')
    is_active = factory.Faker('boolean')

    @factory.post_generation
    def stations(self, create, extracted, **kwargs):
        if not create:
            # Simple build, do nothing.
            return

        if extracted:
            # A list of groups were passed in, use them
            for station in extracted:
                self.stations.add(station)

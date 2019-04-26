# coding: utf-8
import factory
from factory import Faker, SubFactory
from factory.django import DjangoModelFactory

from apps.lines.models import LineModel, RouteModel


class LineFactory(DjangoModelFactory):

    class Meta:
        model = LineModel

    name = Faker('slug')
    color = Faker('slug')


class RouteFactory(DjangoModelFactory):

    class Meta:
        model = RouteModel

    line = SubFactory(LineFactory)
    direction = Faker('boolean')
    is_active = Faker('boolean')

    @factory.post_generation
    def stations(self, create, extracted, **kwargs):
        if not create:
            return

        if extracted:
            # A list of stations were passed in, use them
            for station in extracted:
                self.stations.add(station)

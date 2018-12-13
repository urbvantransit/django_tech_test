# coding: utf8
import factory

from apps.stations.factories import LocationFactory
from .models import (LineModel, RouteModel)


class LineFactory(factory.django.DjangoModelFactory):

    class Meta:
        model = LineModel

    name = factory.Faker('name')
    color = '#0000FF'

class DummyLineFactory(factory.django.DjangoModelFactory):

    class Meta:
        model = LineModel

    name = factory.Sequence(lambda n: 'Dummy Line {}'.format(n))
    color = '#0000FF'

class RouteFactory(factory.django.DjangoModelFactory):

    class Meta:
        model = RouteModel

    line = factory.SubFactory(DummyLineFactory)
    @factory.post_generation
    def stations(self, create, extracted, **kwargs):
        if not create:
            # Simple build, do nothing.
            return

        if extracted:
            # A list of groups were passed in, use them
            for station in extracted:
                self.stations.add(station)
    direction = True
    is_active = True

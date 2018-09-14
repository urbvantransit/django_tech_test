# coding: utf8
import factory

from apps.stations.factories import StationFactory
from . import models


class LineFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models.LineModel

    name = factory.Faker('street_name')
    color = factory.Faker('hex_color')


class RouteFactory(factory.django.DjangoModelFactory):
    """RouteFactory(stations__num: int = 1)

    Routes factory for testing, will have `stations__num` factory-made Stations associated with this route
    """
    class Meta:
        model = models.RouteModel

    line = factory.SubFactory(LineFactory)
    direction = factory.Faker('boolean')
    is_active = factory.Faker('boolean')

    @factory.post_generation
    def stations(self, create, unused, **kwargs):
        if not create:
            return
        else:
            num_stations = kwargs.get('num', 1)
            for _ in range(num_stations):
                sta = StationFactory()
                self.stations.add(sta)

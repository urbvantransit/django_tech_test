# coding: utf8
import factory
from faker import Factory
from .models import LineModel, RouteModel

faker = Factory.create()


class LineFactory(factory.django.DjangoModelFactory):

    class Meta:
        model = LineModel

    name = factory.Faker('name')
    color = factory.Faker('slug')


class RouteFactory(factory.django.DjangoModelFactory):

    class Meta:
        model = RouteModel

    line = factory.SubFactory(LineFactory)
    direction = True
    is_active = True

    @factory.post_generation
    def stations(self, create, extracted, **kwargs):
        if not create:
            return
        if extracted:
            # A list of groups were passed in, use them
            for stations in extracted:
                self.stations.add(stations)

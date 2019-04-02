# coding: utf8
import factory

from .models import LineModel, RouteModel


class LineFactory(factory.django.DjangoModelFactory):
    name = factory.Faker("slug")
    color = factory.Faker('slug')

    class Meta:
        model = LineModel


class RouteFactory(factory.django.DjangoModelFactory):
    direction = factory.Faker('boolean')
    is_active = factory.Faker('boolean')
    line = factory.SubFactory(LineFactory)

    class Meta:
        model = RouteModel

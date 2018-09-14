# coding: utf8

from rest_framework.viewsets import ModelViewSet

from . import models
from . import serializers


class LineViewSet(ModelViewSet):
    queryset = models.LineModel.objects.all()
    serializer_class = serializers.LineSerializer


class RouteViewSet(ModelViewSet):
    queryset = models.RouteModel.objects.all()
    serializer_class = serializers.RouteSerializer

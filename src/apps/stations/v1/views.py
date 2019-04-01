# coding: utf8
from urbvan_framework.views import DetailView, ListCreateView

from .schemas import LocationSchema
from .serializers import LocationSerializer
from ..models import LocationModel


class BaseLocationView(object):
    queryset = LocationModel.objects.all().order_by('name')
    schema_class = LocationSchema
    serializer_class = LocationSerializer


class LocationView(BaseLocationView, ListCreateView):
    pass


class LocationDetailView(BaseLocationView, DetailView):
    pass

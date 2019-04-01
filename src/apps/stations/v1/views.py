# coding: utf8
from urbvan_framework.views import DetailView, ListCreateView

from .schemas import LocationSchema, StationSchema
from .serializers import LocationSerializer, StationSerializer
from ..models import LocationModel, StationModel


class BaseLocationView(object):
    queryset = LocationModel.objects.all().order_by('name')
    schema_class = LocationSchema
    serializer_class = LocationSerializer


class LocationView(BaseLocationView, ListCreateView):
    pass


class LocationDetailView(BaseLocationView, DetailView):
    pass


class BaseStationView(object):
    queryset = StationModel.objects.all().order_by('order')
    schema_class = StationSchema
    serializer_class = StationSerializer


class StationView(BaseStationView, ListCreateView):
    pass


class StationDetailView(BaseStationView, DetailView):
    pass

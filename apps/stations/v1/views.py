# coding: utf8
from urbvan_framework.views import ListCreateView,UpdateView,DestroyView

from .schemas import LocationSchema,StationSchema
from .serializers import LocationSerializer,StationSerializer
from ..models import LocationModel,StationModel


class LocationView(ListCreateView):
    queryset = LocationModel.objects.all()
    schema_class = LocationSchema
    serializer_class = LocationSerializer

class LocationUpdateView(UpdateView):
    queryset = LocationModel.objects.all()
    schema_class = LocationSchema
    serializer_class = LocationSerializer

class LocationDestroyView(DestroyView):
    queryset = LocationModel.objects.all()
    schema_class = LocationSchema
    serializer_class = LocationSerializer

class StationView(ListCreateView):
    queryset = StationModel.objects.all()
    schema_class = StationSchema
    serializer_class = StationSerializer

class StationUpdateView(UpdateView):
    queryset = StationModel.objects.all()
    schema_class = StationSchema
    serializer_class = StationSerializer

class StationDestroyView(DestroyView):
    queryset = StationModel.objects.all()
    schema_class = StationSchema
    serializer_class = StationSerializer
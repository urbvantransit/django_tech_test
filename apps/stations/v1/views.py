# coding: utf8
from urbvan_framework.views import (ListCreateView, DetailView)

from .schemas import (LocationSchema, StationSchema)
from .serializers import (LocationSerializer, StationSerializer)
from ..models import (LocationModel,StationModel)


class LocationListCreateView(ListCreateView):
    """
        List view for thew Location model
    """
    queryset = LocationModel.objects.all()
    schema_class = LocationSchema
    serializer_class = LocationSerializer


class LocationDetailView(DetailView):
    """
        Detail view for thew Location model
    """
    queryset = LocationModel.objects.none()
    model = LocationModel
    schema_class = LocationSchema
    serializer_class = LocationSerializer


class StationListCreateView(ListCreateView):
    """
        List view for thew Station model
    """
    queryset = StationModel.objects.all()
    model = StationModel
    schema_class = StationSchema
    serializer_class = StationSerializer


class StationDetailView(DetailView):
    """
        Detail view for thew Station model
    """
    queryset = StationModel.objects.none()
    model = StationModel
    schema_class = StationSchema
    serializer_class = StationSerializer

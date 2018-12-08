# coding: utf8
from urbvan_framework.views import (ListCreateView,
    RetrieveUpdateDestroyAPIView)

from .schemas import (LocationSchema, StationSchema)
from .serializers import (LocationSerializer, StationSerializer)

from ..models import (LocationModel, StationModel)


class LocationView(ListCreateView):

    queryset = LocationModel.objects.all()
    schema_class = LocationSchema
    serializer_class = LocationSerializer


class LocationRUDView(RetrieveUpdateDestroyAPIView):

    queryset = LocationModel.objects.all()
    schema_class = LocationSchema
    serializer_class = LocationSerializer


class StationView(ListCreateView):

    queryset = StationModel.objects.all()
    schema_class = StationSchema
    serializer_class = StationSerializer


class StationRUDView(RetrieveUpdateDestroyAPIView):

    queryset = StationModel.objects.all()
    schema_class = StationSchema
    serializer_class = StationSerializer

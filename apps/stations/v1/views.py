# coding: utf8
from urbvan_framework.views import ListCreateView

from ..models import LocationModel
from .schemas import LocationSchema
from .serializers import LocationSerializer


class LocationView(ListCreateView):

    queryset = LocationModel.objects.all()
    schema_class = LocationSchema
    serializer_class = LocationSerializer

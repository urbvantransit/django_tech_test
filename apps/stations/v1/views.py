# coding: utf8
from urbvan_framework.views import ListCreateView
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from .schemas import LocationSchema
from .serializers import LocationSerializer

from ..models import LocationModel


class LocationView(generics.ListCreateAPIView):
    queryset = LocationModel.objects.all()
    schema_class = LocationSchema
    serializer_class = LocationSerializer
    permission_classes = (IsAuthenticated,)

class LocationViewDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = LocationModel.objects.all()
    schema_class = LocationSchema
    serializer_class = LocationSerializer
    permission_classes = (IsAuthenticated,)
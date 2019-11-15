# coding: utf8
from urbvan_framework.views import (
    ListCreateView,
    IsStaffUser,
    IsAnonymousUser,
    IsSuperUser,
)
from rest_framework.generics import (
    ListAPIView,
    CreateAPIView,
    RetrieveAPIView,
    DestroyAPIView,
)
from urbvan_framework.authentication import CustomTokenAuthentication
from .schemas import LocationSchema, StationSchema
from rest_framework.permissions import IsAuthenticated
from .serializers import LocationSerializer, StationSerializer

from ..models import LocationModel, StationModel


class LocationView(ListCreateView):

    queryset = LocationModel.objects.all()
    schema_class = LocationSchema
    serializer_class = LocationSerializer


"""
Station CRUD views
 - List 
 - Retrive
 - Create
 - Delete
"""


class StationModelListView(ListAPIView):

    authentication_classes = (CustomTokenAuthentication,)
    permission_classes = (IsAnonymousUser,)

    queryset = StationModel.objects.all()
    schema_class = StationSchema
    serializer_class = StationSerializer


class StationModelDetailView(RetrieveAPIView):

    authentication_classes = (CustomTokenAuthentication,)
    permission_classes = (
        IsAuthenticated,
        IsStaffUser,
    )

    queryset = StationModel.objects.all()
    schema_class = StationSchema
    serializer_class = StationSerializer


class StationModelCreateView(CreateAPIView):

    authentication_classes = (CustomTokenAuthentication,)
    permission_classes = (
        IsAuthenticated,
        IsSuperUser,
    )

    serializer_class = StationSerializer
    schema_class = StationSchema


class StationModelDeleteView(DestroyAPIView):

    authentication_classes = (CustomTokenAuthentication,)
    permission_classes = (
        IsAuthenticated,
        IsSuperUser,
    )

    queryset = StationModel.objects.all()
    schema_class = StationSchema
    serializer_class = StationSerializer

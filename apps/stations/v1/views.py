# coding: utf8
from urbvan_framework import views

from apps.users.permissions import IsTier2, IsTier3

from .schemas import LocationSchema, StationSchema
from .serializers import LocationSerializer, LocationSerializerId, \
    StationSerializer, StationSerializerId

from ..models import LocationModel, StationModel


class LocationListView(views.ListAPIView):

    queryset = LocationModel.objects.all()
    schema_class = LocationSchema
    serializer_class = LocationSerializerId


class LocationCreateView(views.CreateAPIView):
    queryset = LocationModel.objects.all()
    schema_class = LocationSchema
    serializer_class = LocationSerializer


class LocationRetrieveView(views.RetrieveAPIView):
    queryset = LocationModel.objects.all()
    schema_class = LocationSchema
    serializer_class = LocationSerializerId
    permission_classes = (IsTier2,)


class LocationUpdateView(views.UpdateAPIView):
    queryset = LocationModel.objects.all()
    schema_class = LocationSchema
    serializer_class = LocationSerializerId
    permission_classes = (IsTier2,)


class LocationDestroyView(views.DestroyAPIView):
    queryset = LocationModel.objects.all()
    schema_class = LocationSchema
    serializer_class = LocationSerializerId
    permission_classes = (IsTier3,)


class LocationListCreateView(views.BaseManageView):
        VIEWS_BY_METHOD = {
        'POST': LocationCreateView.as_view,
        'GET': LocationListView.as_view,
    }

class LocationManageView(views.BaseManageView):
        VIEWS_BY_METHOD = {
        'DELETE': LocationDestroyView.as_view,
        'GET': LocationRetrieveView.as_view,
        'PUT': LocationUpdateView.as_view,
        'PATCH': LocationUpdateView.as_view
    }


class StationListView(views.ListAPIView):
    queryset = StationModel.objects.all()
    schema_class = StationSchema
    serializer_class = StationSerializerId


class StationCreateView(views.CreateAPIView):
    queryset = StationModel.objects.all()
    schema_class = StationSchema
    serializer_class = StationSerializer


class StationRetrieveView(views.RetrieveAPIView):
    queryset = StationModel.objects.all()
    schema_class = StationSchema
    serializer_class = StationSerializerId
    permission_classes = (IsTier2,)


class StationUpdateView(views.UpdateAPIView):
    queryset = StationModel.objects.all()
    schema_class = StationSchema
    serializer_class = StationSerializerId
    permission_classes = (IsTier2,)


class StationDestroyView(views.DestroyAPIView):
    queryset = StationModel.objects.all()
    schema_class = StationSchema
    serializer_class = StationSerializerId
    permission_classes = (IsTier3,)

class StationListCreateView(views.BaseManageView):
        VIEWS_BY_METHOD = {
        'POST': StationCreateView.as_view,
        'GET': StationListView.as_view,
    }

class StationManageView(views.BaseManageView):
        VIEWS_BY_METHOD = {
        'DELETE': StationDestroyView.as_view,
        'GET': StationRetrieveView.as_view,
        'PUT': StationUpdateView.as_view,
        'PATCH': StationUpdateView.as_view
    }
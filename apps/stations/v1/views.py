# coding: utf8
from urbvan_framework.views import ListCreateView,\
                                                       UpdateView,\
                                                       DestroyView,\
                                                       ListAPIView,\
                                                       CreateAPIView\

from .schemas import LocationSchema, StationSchema
from .serializers import LocationSerializer, StationSerializer

from ..models import LocationModel, StationModel
from ...users.permissions import BasicUser, StaffUser, SuperUser


class LocationView(ListCreateView):

    queryset = LocationModel.objects.order_by('id').all()
    schema_class = LocationSchema
    serializer_class = LocationSerializer
    permission_classes = (StaffUser, )


class LocationUpdateView(UpdateView):
    queryset = LocationModel.objects.order_by('id').all()
    schema_class = LocationSchema
    serializer_class = LocationSerializer
    permission_classes = (StaffUser, )


class LocationDestroyView(DestroyView):

    queryset = LocationModel.objects.order_by('id').all()
    schema_class = LocationSchema
    serializer_class = LocationSerializer
    permission_classes = (SuperUser, )


class StationListView(ListAPIView):

    queryset = StationModel.objects.order_by('id').all()
    schema_class = StationSchema
    serializer_class = StationSchema
    permission_classes = (BasicUser, )

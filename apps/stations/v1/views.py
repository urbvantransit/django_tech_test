# coding: utf8
from urbvan_framework.views import ListCreateView, UpdateView, DestroyView

from .schemas import LocationSchema
from .serializers import LocationSerializer

from ..models import LocationModel
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

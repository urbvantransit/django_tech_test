# coding: utf8
from urbvan_framework.views import ListCreateView,UpdateView,DestroyView

from .schemas import LocationSchema,StationSchema
from .serializers import LocationSerializer,StationSerializer
from ..models import LocationModel,StationModel
"""
Views related to :model:`stations.StationModel` and
:model:`stations.LocationModel`.
"""

class LocationView(ListCreateView):
    """
    GET and POST for :model:`stations.LocationModel`
    child of ListCreateView related to Urbvan 
    Framework.

    **Context**

    ``queryset``
        Queryset of all :model:`stations.LocationModel` objects
    ``schema_class``
        Schema of :model:`stations.LocationModel`
    ``serializer_class``
        Serializer of :model:`stations.LocationModel`
    """
    queryset = LocationModel.objects.all()
    schema_class = LocationSchema
    serializer_class = LocationSerializer

class LocationUpdateView(UpdateView):
    """
    Update `stations.LocationModel`
    child of UpdateView related to Urbvan 
    Framework.

    **Context**

    ``queryset``
        Queryset of all `stations.LocationModel` objects
    ``schema_class``
        Schema of `stations.LocationModel`
    ``serializer_class``
        Serializer of `stations.LocationModel` 
    """
    queryset = LocationModel.objects.all()
    schema_class = LocationSchema
    serializer_class = LocationSerializer

class LocationDestroyView(DestroyView):
    """
    Delete `stations.LocationModel`
    child of UpdateView related to Urbvan 
    Framework.

    **Context**

    ``queryset``
        Queryset of all `stations.LocationModel` objects
    ``schema_class``
        Schema of `stations.LocationModel`
    ``serializer_class``
        Serializer of `stations.LocationModel`
    """
    queryset = LocationModel.objects.all()
    schema_class = LocationSchema
    serializer_class = LocationSerializer

class StationView(ListCreateView):
    """
    GET and POST for :model:`stations.StationModel`
    child of ListCreateView related to Urbvan 
    Framework.

    **Context**

    ``queryset``
        Queryset of all :model:`stations.StationModel` objects
    ``schema_class``
        Schema of :model:`stations.StationModel`
    ``serializer_class``
        Serializer of :model:`stations.StationModel`
    """
    queryset = StationModel.objects.all()
    schema_class = StationSchema
    serializer_class = StationSerializer

class StationUpdateView(UpdateView):
    """
    Update :model:`stations.StationModel`
    child of UpdateView related to Urbvan 
    Framework.

    **Context**

    ``queryset``
        Queryset of all :model:`stations.StationModel` objects
    ``schema_class``
        Schema of :model:`stations.StationModel`
    ``serializer_class``
        Serializer of :model:`stations.StationModel` 
    """
    queryset = StationModel.objects.all()
    schema_class = StationSchema
    serializer_class = StationSerializer

class StationDestroyView(DestroyView):
    """
    Delete :model:`stations.StationModel`
    child of UpdateView related to Urbvan 
    Framework.

    **Context**

    ``queryset``
        Queryset of all :model:`stations.StationModel` objects
    ``schema_class``
        Schema of :model:`stations.StationModel`
    ``serializer_class``
        Serializer of :model:`stations.StationModel`
    """
    queryset = StationModel.objects.all()
    schema_class = StationSchema
    serializer_class = StationSerializer
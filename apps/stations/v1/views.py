# coding: utf8
from urbvan_framework.views import ListCreateView
from rest_framework import generics, mixins
from .schemas import LocationSchema, StationSchema
from .serializers import LocationSerializer, StationSerializer
from urbvan_framework.authentication import CustomTokenAuthentication
from rest_framework.permissions import IsAuthenticated

from ..models import LocationModel, StationModel


class LocationView(ListCreateView):

    queryset = LocationModel.objects.all()
    schema_class = LocationSchema
    serializer_class = LocationSerializer

'''
Vista de detalle para Locaton

Se agrega funcionalidad para eliminar y actualizar en base al id
'''
class LocationDetailView(mixins.DestroyModelMixin, mixins.UpdateModelMixin, generics.RetrieveAPIView):
    authentication_classes = (CustomTokenAuthentication,)
    permission_classes = (IsAuthenticated,)
    serializer_class = LocationSerializer
    queryset = LocationModel.objects.all()

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, *kwargs)
    
    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, *kwargs)


'''
Listar Staciones

Se agrega funconalidad para crear nuevas estaciones
'''
class StationView(ListCreateView):

    queryset = StationModel.objects.all()
    schema_class = StationSchema
    serializer_class = StationSerializer

'''
Vista de detalle Station

Se agrega funcionalidad para eliminar, actualizar y ver el detalle en base al id
'''
class StationDetailView(mixins.DestroyModelMixin, mixins.UpdateModelMixin, generics.RetrieveAPIView):
    authentication_classes = (CustomTokenAuthentication,)
    permission_classes = (IsAuthenticated,)
    serializer_class = StationSerializer
    queryset = StationModel.objects.all()

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, *kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, *kwargs)

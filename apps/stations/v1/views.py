# coding: utf8
from rest_framework import generics, status
from rest_framework.response import Response

from urbvan_framework.authentication import CustomTokenAuthentication
from urbvan_framework.utils import render_response_error, render_to_response
from urbvan_framework.views import ListCreateView

from ..models import LocationModel, StationModel
from .schemas import LocationSchema, StationSchema
from .serializers import LocationSerializer, StationSerializer

# ********** Location Views *************

class LocationView(ListCreateView):
    """
    Vista concreta que permite listar y crear `Locations`
    en una misma vista, haciendo uso de métodos GET y POST
    """

    queryset = LocationModel.objects.all()
    schema_class = LocationSchema
    serializer_class = LocationSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class RUDLocationAPIView(generics.RetrieveUpdateDestroyAPIView):
    """
    Vista concreta que permite:
    - retonar un objeto (GET) - Location
    - Actualizar un objeto (PATCH/PUT) - Location
    - Eliminar un objeto (DELETE) - Location
    con el ID del objeto/registro
    """
    queryset = LocationModel.objects.all()
    schema_class = LocationSchema
    serializer_class = LocationSerializer
    authentication_classes = (CustomTokenAuthentication, )
    lookup_field = ('id')

    def retrieve(self, request,*args, **kwargs):
        super(RUDLocationAPIView, self).retrieve(request, args, kwargs)
        instance = self.get_object()
        serializer = self.get_serializer(instance, context={'request':request})
        data = serializer.data
        response = render_to_response(body=data)
        return Response(response, status=status.HTTP_200_OK)

    def patch(self, request,*args, **kwargs):
        super(RUDLocationAPIView, self).patch(request, args, kwargs)
        instance = self.get_object()
        serializer = self.get_serializer(instance, context={'request':request})
        data = serializer.data
        response = render_to_response(body=data)
        return Response(response, status=status.HTTP_200_OK)

    def delete(self, request,*args, **kwargs):
        super(RUDLocationAPIView, self).delete(request, args, kwargs)
        return Response(data={'message': "Eliminado con éxito"}, status=status.HTTP_204_NO_CONTENT)

# ************ Stations Views **********
class StationView(ListCreateView):
    """
    Vista concreta que permite listar y crear `Stations`
    en una misma vista, haciendo uso de métodos GET y POST
    """

    queryset = StationModel.objects.all()
    schema_class = StationSchema
    serializer_class = StationSerializer

    def perform_create(self, serializer):
        """
        Esta función permite que al crear un nuevo registro (objeto),
        el usuario se quede guardado con su id, para posteriormente hacer
        validaciones.
        """
        serializer.save(user=self.request.user)


class RUDStationAPIView(generics.RetrieveUpdateDestroyAPIView):
    """
    Vista concreta que permite:
    - retonar un objeto (GET) - Station
    - Actualizar un objeto (PATCH/PUT) - Station
    - Eliminar un objeto (DELETE) - Station
    con el ID del objeto/registro
    """
    queryset = StationModel.objects.all()
    schema_class = StationSchema
    serializer_class = StationSerializer
    authentication_classes = (CustomTokenAuthentication, )
    lookup_field = ('id')

    def retrieve(self, request,*args, **kwargs):
        super(RUDStationAPIView, self).retrieve(request, args, kwargs)
        instance = self.get_object()
        serializer = self.get_serializer(instance, context={'request':request})
        data = serializer.data
        response = render_to_response(body=data)
        return Response(response, status=status.HTTP_200_OK)

    def patch(self, request,*args, **kwargs):
        super(RUDStationAPIView, self).patch(request, args, kwargs)
        instance = self.get_object()
        serializer = self.get_serializer(instance, context={'request':request})
        data = serializer.data
        response = render_to_response(body=data)
        return Response(response, status=status.HTTP_200_OK)

    def delete(self, request,*args, **kwargs):
        super(RUDStationAPIView, self).delete(request, args, kwargs)
        return Response(data={'message': "Eliminado con éxito"}, status=status.HTTP_204_NO_CONTENT)

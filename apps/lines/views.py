from django.shortcuts import render, get_object_or_404

from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import generics

from .models import LineModel, RouteModel
from .serializers import LineSerializer
# Create your views here.
    
class LineView(generics.ListAPIView):
    permission_classes      = []
    authentication_classes  = []

    queryset                = LineModel.objects.all()
    serializer_class        = LineSerializer

    def get_queryset(self):
        qs = LineModel.objects.all()
        query = self.request.GET.get('q') # leer el paremetro GET de la ruta
        if query is not None:
            qs = qs.filter(name__icontains = query) #filtrar el nombre por el parametro en la ruta
        
        return qs

class LineCreateView(generics.CreateAPIView):
    permission_classes      = []
    authentication_classes  = []
    serializer_class        = LineSerializer

class LineDetailView(generics.RetrieveAPIView):
    permission_classes      = []
    authentication_classes  = []
    serializer_class        = LineSerializer
    queryset                = LineModel.objects.all()
    lookup_field            = id

    def get_object(self, *args, **kwargs):
        kwargs = self.kwargs # parametros por teclado
        kw_id = kwargs.get('id') # obtener el parametro id de los parametros por telcado
        return LineModel.objects.get(id = kw_id) # retornar solo el objeto que tenga el id = kw_id

class LineUpdateView(generics.UpdateAPIView):
    permission_classes      = []
    authentication_classes  = []
    serializer_class        = LineSerializer
    queryset                = LineModel.objects.all()

class LineDeleteView(generics.DestroyAPIView):
    permission_classes      = []
    authentication_classes  = []
    serializer_class        = LineSerializer
    queryset                = LineModel.objects.all()
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status, generics
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly

from apps.lines.serializers import LineSerializer, RouteModelSerailizer
from apps.lines.models import LineModel, RouteModel
# Create your views here.

class ListCreateLineView(generics.ListCreateAPIView):
    """
    Clase que permite crear una nueva linea o listar 
    todas las lineas existentes.
    """
    queryset = LineModel.objects.all()
    serializer_class = LineSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
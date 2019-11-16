from django.http import Http404
from rest_framework import generics, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from apps.lines.models import LineModel, RouteModel
from apps.lines.serializers import LineSerializer, RouteModelSerailizer
# from apps.core.permissions import superuser_only
from urbvan_framework.authentication import CustomTokenAuthentication
from urbvan_framework.schemas import PaginationResponse
from urbvan_framework.utils import render_response_error, render_to_response

# from django.utils.decorators import method_decorator


# Create your views here.

# ****** LineModel ******* 
class ListCreateLineAPIView(generics.ListCreateAPIView):
    """
    Vista que permite crear y listar `Lines` en una sola,
    sólo cambiando el método de petición HTTP (GET & POST)
    """
    queryset = LineModel.objects.all().order_by('-createdAt')
    serializer_class = LineSerializer
    permission_classes = (IsAuthenticated, )
    authentication_classes = (CustomTokenAuthentication,)
    pagination_class = PaginationResponse

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class RetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    """
    Vista concreta que permite `Traer`, `Actualizar` y `Eliminar`
    `Lines` desde una misma vista, con los métodos:
    (GET, PATCH/PUT & DELETE)
    """
    queryset = LineModel.objects.all()
    serializer_class = LineSerializer
    permission_classes = (IsAuthenticated, )
    authentication_classes = (CustomTokenAuthentication,)
    lookup_field = 'id'

    def retrieve(self, request,*args, **kwargs):
        super(RetrieveUpdateDestroyAPIView, self).retrieve(request, args, kwargs)
        instance = self.get_object()
        serializer = self.get_serializer(instance, context={'request':request})
        data = serializer.data
        response = render_to_response(body=data)
        return Response(response, status=status.HTTP_200_OK)

    def patch(self, request,*args, **kwargs):
        super(RetrieveUpdateDestroyAPIView, self).patch(request, args, kwargs)
        instance = self.get_object()
        serializer = self.get_serializer(instance, context={'request':request})
        data = serializer.data
        response = render_to_response(body=data)
        return Response(response, status=status.HTTP_200_OK)

    def delete(self, request,*args, **kwargs):
        super(RetrieveUpdateDestroyAPIView, self).delete(request, args, kwargs)
        
        return Response(data={'message': "Eliminado con éxito"}, status=status.HTTP_204_NO_CONTENT)

# ****** RouteModel ******* 
class ListCreateRouteAPIView(generics.ListCreateAPIView):
    """
    Vista que permite crear y listar `Routes` en una sola,
    sólo cambiando el método de petición HTTP (GET & POST)
    """
    queryset = RouteModel.objects.all().order_by('-createdAt')
    serializer_class = RouteModelSerailizer
    permission_classes = (IsAuthenticated, )
    authentication_classes = (CustomTokenAuthentication,)
    pagination_class = PaginationResponse

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class RetrieveUpdateDestroyRouteAPIView(generics.RetrieveUpdateDestroyAPIView):
    """
    Vista concreta que permite `Traer`, `Actualizar` y `Eliminar`
    `Lines` desde una misma vista, con los métodos:
    (GET, PATCH/PUT & DELETE)
    """
    queryset = RouteModel.objects.all()
    serializer_class = RouteModelSerailizer
    permission_classes = (IsAuthenticated, )
    authentication_classes = (CustomTokenAuthentication,)
    lookup_field = 'id'

    def retrieve(self, request,*args, **kwargs):
        super(RetrieveUpdateDestroyRouteAPIView, self).retrieve(request, args, kwargs)
        instance = self.get_object()
        serializer = self.get_serializer(instance, context={'request':request})
        data = serializer.data
        response = render_to_response(body=data)
        return Response(response, status=status.HTTP_200_OK)

    def patch(self, request,*args, **kwargs):
        super(RetrieveUpdateDestroyRouteAPIView, self).patch(request, args, kwargs)
        instance = self.get_object()
        serializer = self.get_serializer(instance, context={'request':request})
        data = serializer.data
        response = render_to_response(body=data)
        return Response(response, status=status.HTTP_200_OK)

    def delete(self, request,*args, **kwargs):
        super(RetrieveUpdateDestroyRouteAPIView, self).delete(request, args, kwargs)
        
        return Response(data={'message': "Eliminado con éxito"}, status=status.HTTP_204_NO_CONTENT)

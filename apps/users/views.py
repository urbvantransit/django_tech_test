from rest_framework import status, permissions
from rest_framework.views import APIView
from rest_framework.response import Response

from .serializers import UserCreateSerializer
from urbvan_framework.utils import render_to_response

class RegisterUserAPIView(APIView):
    """
    Clase que permite crear un nuevo usuario y su perfil,
    si `is_driver` está marcado y/o es True, entonces se crea
    un perfil para `driver`, de lo contrario, crea un perfil
    de usuario normal (Pasajero de Urbvan)
    """
    permission_classes = (permissions.AllowAny, )

    def post(self, request, format=None):
        serializer = UserCreateSerializer(data = request.data or None)
        if serializer.is_valid():
            serializer.save()
            return Response(
                data={'message': 'Se ha registrado con éxito'},
                status=status.HTTP_201_CREATED
            )
        else:
            return Response(
                data={'errors': serializer._errors},
                status=status.HTTP_400_BAD_REQUEST
            )

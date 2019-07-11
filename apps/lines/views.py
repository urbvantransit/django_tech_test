
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
# importar modelos
from .models import LineModel, RouteModel
#importar serializers
from .serializers import LineSerializer, RouteSerializer
from .schemas import LineSchema, RouteSchema
#urbvan framework
from urbvan_framework.views import ListCreateView

from urbvan_framework.authentication import CustomTokenAuthentication 
############## Vistas para modelo LineModel
'''
Listar todas las lineas 
'''  


class LineView(ListCreateView):
    authentication_classes = (CustomTokenAuthentication,)
    permission_classes = (IsAuthenticated,)
    schema_class = LineSchema
    queryset                = LineModel.objects.all()
    serializer_class        = LineSerializer

    def get_queryset(self):
        qs = LineModel.objects.all()
        query = self.request.GET.get('q') # leer el paremetro GET de la ruta
        if query is not None:
            qs = qs.filter(name__icontains = query) #filtrar el nombre por el parametro en la ruta
        
        return qs
'''
Crear una nueva linea
'''
class LineCreateView(generics.CreateAPIView):
    authentication_classes = (CustomTokenAuthentication,)
    permission_classes = (IsAuthenticated,)
    serializer_class        = LineSerializer
'''
Ver el detalle de una linea por el id
'''
class LineDetailView(generics.RetrieveAPIView):
    authentication_classes = (CustomTokenAuthentication,)
    permission_classes = (IsAuthenticated,)
    serializer_class        = LineSerializer
    queryset                = LineModel.objects.all()
    lookup_field            = id

    def get_object(self, *args, **kwargs):
        kwargs = self.kwargs # parametros por teclado
        kw_id = kwargs.get('id') # obtener el parametro id de los parametros por telcado
        return LineModel.objects.get(id = kw_id) # retornar solo el objeto que tenga el id = kw_id
'''
Actualizar una linea por el id
'''
class LineUpdateView(generics.UpdateAPIView):
    authentication_classes = (CustomTokenAuthentication,)
    permission_classes = (IsAuthenticated,)
    serializer_class        = LineSerializer
    queryset                = LineModel.objects.all()
'''
Eliminar una lunea por el id
'''
class LineDeleteView(generics.DestroyAPIView):
    authentication_classes = (CustomTokenAuthentication,)
    permission_classes = (IsAuthenticated,)
    serializer_class        = LineSerializer
    queryset                = LineModel.objects.all()

#################### VIstas para modelo RouteModel


class RouteView(ListCreateView):
    authentication_classes = (CustomTokenAuthentication,)
    permission_classes = (IsAuthenticated,)
    schema_class = RouteSchema
    queryset                = RouteModel.objects.all()
    serializer_class        = RouteSerializer



'''
Crear una nueva Ruta
'''


class RouteCreateView(ListCreateView):
    authentication_classes = (CustomTokenAuthentication,)
    permission_classes = (IsAuthenticated,)
    serializer_class        = RouteSerializer


'''
Ver el detalle de una ruta
'''


class RouteDetailView(generics.RetrieveAPIView):
    authentication_classes = (CustomTokenAuthentication,)
    permission_classes = (IsAuthenticated,)
    serializer_class        = RouteSerializer
    queryset                = RouteModel.objects.all()
    lookup_field            = id

    def get_object(self, *args, **kwargs):
        kwargs = self.kwargs # parametros por teclado
        kw_id = kwargs.get('id') # obtener el parametro id de los parametros por telcado
        return RouteModel.objects.get(id = kw_id) # retornar solo el objeto que tenga el id = kw_id


'''
Actualizar una linea por el id
'''


class RouteUpdateView(generics.UpdateAPIView):
    authentication_classes = (CustomTokenAuthentication,)
    permission_classes = (IsAuthenticated,)
    serializer_class = RouteSerializer
    queryset = RouteModel.objects.all()


'''
Eliminar una lunea por el id
'''


class RouteDeleteView(generics.DestroyAPIView):
    authentication_classes = (CustomTokenAuthentication,)
    permission_classes = (IsAuthenticated,)
    serializer_class = RouteSerializer
    queryset = RouteModel.objects.all()

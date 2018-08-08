# THIRD-PARTY IMPORTS
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated, DjangoModelPermissions

# URBVAN IMPORTS
from urbvan_framework.authentication import CustomTokenAuthentication
from .serializers import (
    LineModelSerializer,
    RouteModelSerializer,
)
from ..models import (
    LineModel,
    RouteModel,
)


class LineModelViewset(viewsets.ModelViewSet):
    '''
        CRUD for LineModel
        @author: Christianbos
    '''
    queryset = LineModel.objects.all()
    serializer_class = LineModelSerializer
    authentication_classes = (CustomTokenAuthentication,)
    permission_classes = (IsAuthenticated, )


class RouteModelViewset(viewsets.ModelViewSet):
    '''
        CRUD for RouteModel
        @author: Christianbos
    '''
    queryset = RouteModel.objects.all()
    serializer_class = RouteModelSerializer
    authentication_classes = (CustomTokenAuthentication,)
    permission_classes = (IsAuthenticated,)
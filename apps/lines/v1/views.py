# coding: utf8
from urbvan_framework.views import (ListCreateView,
    RetrieveUpdateDestroyAPIView)

from .schemas import (LineSchema, RouteSchema)
from .serializers import (LineSerializer, RouteSerializer)

from ..models import (LineModel, RouteModel)


class LineView(ListCreateView):

    queryset = LineModel.objects.all()
    schema_class = LineSchema
    serializer_class = LineSerializer
    model_crud_permissions = LineModel


class LineRUDView(RetrieveUpdateDestroyAPIView):

    queryset = LineModel.objects.all()
    schema_class = LineSchema
    serializer_class = LineSerializer
    model_crud_permissions = LineModel


class RouteView(ListCreateView):

    queryset = RouteModel.objects.all()
    schema_class = RouteSchema
    serializer_class = RouteSerializer
    model_crud_permissions = RouteModel


class RouteRUDView(RetrieveUpdateDestroyAPIView):

    queryset = RouteModel.objects.all()
    schema_class = RouteSchema
    serializer_class = RouteSerializer
    model_crud_permissions = RouteModel

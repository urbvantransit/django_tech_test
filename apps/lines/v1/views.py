# coding: utf8
from urbvan_framework.views import (ListCreateView, DetailView)
from .schemas import (LineSchema, RouteSchema)
from .serializers import (LineSerializer, RouteSerializer)
from ..models import (LineModel, RouteModel)


class LineView(ListCreateView):
    """
        List view for thew Line model
    """
    queryset = LineModel.objects.all()
    schema_class = LineSchema
    serializer_class = LineSerializer


class LineDetailView(DetailView):
    """
        Detail view for thew Line model
    """
    queryset = LineModel.objects.none()
    model = LineModel
    schema_class = LineSchema
    serializer_class = LineSerializer


class RouteView(ListCreateView):
    """
        List view for thew Route model
    """
    queryset = RouteModel.objects.all()
    schema_class = RouteSchema
    serializer_class = RouteSerializer


class RouteDetailView(DetailView):
    """
        Detail view for thew Line model
    """
    queryset = RouteModel.objects.none()
    model = RouteModel
    schema_class = RouteSchema
    serializer_class = RouteSerializer

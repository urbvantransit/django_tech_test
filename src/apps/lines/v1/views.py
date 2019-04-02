# coding: utf8
from urbvan_framework.views import DetailView, ListCreateView

from .schemas import LineSchema, RouteSchema
from .serializers import LineSerializer, RouteSerializer
from ..models import LineModel, RouteModel


class BaseLineView(object):
    queryset = LineModel.objects.all().order_by('name')
    schema_class = LineSchema
    serializer_class = LineSerializer


class LineView(BaseLineView, ListCreateView):
    pass


class LineDetailView(BaseLineView, DetailView):
    pass


class BaseRouteView(object):
    queryset = RouteModel.objects.all().order_by('id')
    schema_class = RouteSchema
    serializer_class = RouteSerializer


class RouteView(BaseRouteView, ListCreateView):
    pass


class RouteDetailView(BaseRouteView, DetailView):
    pass

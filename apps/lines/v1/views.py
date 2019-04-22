# coding: utf8
from urbvan_framework import views

from apps.users.permissions import IsTier2, IsTier3
from rest_framework.permissions import AllowAny

from .schemas import LineSchema, RouteSchema
from .serializers import LineSerializer, LineSerializerId, \
    RouteSerializer, RouteSerializerId

from ..models import LineModel, RouteModel


class LineListView(views.ListAPIView):

    queryset = LineModel.objects.all()
    schema_class = LineSchema
    serializer_class = LineSerializerId


class LineCreateView(views.CreateAPIView):
    queryset = LineModel.objects.all()
    schema_class = LineSchema
    serializer_class = LineSerializer


class LineRetrieveView(views.RetrieveAPIView):
    queryset = LineModel.objects.all()
    schema_class = LineSchema
    serializer_class = LineSerializerId
    permission_classes = (IsTier2,)


class LineUpdateView(views.UpdateAPIView):
    queryset = LineModel.objects.all()
    schema_class = LineSchema
    serializer_class = LineSerializerId
    permission_classes = (IsTier2,)


class LineDestroyView(views.DestroyAPIView):
    queryset = LineModel.objects.all()
    schema_class = LineSchema
    serializer_class = LineSerializerId
    permission_classes = (IsTier3,)


class LineListCreateView(views.BaseManageView):
        VIEWS_BY_METHOD = {
        'POST': LineCreateView.as_view,
        'GET': LineListView.as_view,
    }

class LineManageView(views.BaseManageView):
        VIEWS_BY_METHOD = {
        'DELETE': LineDestroyView.as_view,
        'GET': LineRetrieveView.as_view,
        'PUT': LineUpdateView.as_view,
        'PATCH': LineUpdateView.as_view
    }


class RouteListView(views.ListAPIView):
    queryset = RouteModel.objects.all()
    schema_class = RouteSchema
    serializer_class = RouteSerializerId
    permission_classes = (AllowAny,)


class RouteCreateView(views.CreateAPIView):
    queryset = RouteModel.objects.all()
    schema_class = RouteSchema
    serializer_class = RouteSerializer
    permission_classes = (AllowAny,)


class RouteRetrieveView(views.RetrieveAPIView):
    queryset = RouteModel.objects.all()
    schema_class = RouteSchema
    serializer_class = RouteSerializerId
    permission_classes = (IsTier2,)


class RouteUpdateView(views.UpdateAPIView):
    queryset = RouteModel.objects.all()
    schema_class = RouteSchema
    serializer_class = RouteSerializerId
    permission_classes = (IsTier2,)


class RouteDestroyView(views.DestroyAPIView):
    queryset = RouteModel.objects.all()
    schema_class = RouteSchema
    serializer_class = RouteSerializerId
    permission_classes = (IsTier3,)

class RouteListCreateView(views.BaseManageView):
        VIEWS_BY_METHOD = {
        'POST': RouteCreateView.as_view,
        'GET': RouteListView.as_view,
    }

class RouteManageView(views.BaseManageView):
        VIEWS_BY_METHOD = {
        'DELETE': RouteDestroyView.as_view,
        'GET': RouteRetrieveView.as_view,
        'PUT': RouteUpdateView.as_view,
        'PATCH': RouteUpdateView.as_view
    }
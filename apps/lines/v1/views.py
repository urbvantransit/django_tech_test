from rest_framework.generics import (
    ListAPIView,
    CreateAPIView,
    RetrieveAPIView,
    DestroyAPIView,
)
from apps.lines.models import LineModel
from .serializers import LineModelSerializer
from .schemas import LinesSchema
from rest_framework.permissions import IsAuthenticated
from urbvan_framework.authentication import CustomTokenAuthentication

"""
Lines CRUD views
 - List
 - Retrive
 - Create
 - Delete 
"""


class LineModelListView(ListAPIView):

    authentication_classes = (CustomTokenAuthentication,)
    permission_classes = IsAuthenticated
    queryset = LineModel.objects.all()
    schema_class = LinesSchema
    serializer_class = (
        LineModelSerializer  # TODO:Check if this line is required with Schema
    )


class LineModelDetailView(RetrieveAPIView):

    authentication_classes = (CustomTokenAuthentication,)
    permission_classes = IsAuthenticated

    queryset = LineModel.objects.all()
    schema_class = LinesSchema
    serializer_class = LineModelSerializer


class LineModelCreateView(CreateAPIView):

    authentication_classes = (CustomTokenAuthentication,)
    permission_classes = IsAuthenticated

    serializer_class = LineModelSerializer
    schema_class = LinesSchema


class LineModelDeleteView(DestroyAPIView):

    authentication_classes = (CustomTokenAuthentication,)
    permission_classes = IsAuthenticated

    queryset = LineModel.objects.all()
    schema_class = LinesSchema
    serializer_class = LineModelSerializer

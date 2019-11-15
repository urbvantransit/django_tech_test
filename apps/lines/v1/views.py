from rest_framework.generics import (
    ListAPIView,
    CreateAPIView,
    RetrieveAPIView,
    DestroyAPIView,
)
from apps.lines.models import LineModel, RouteModel
from .serializers import LineModelSerializer, RouteModelSerializer
from .schemas import LinesSchema, RouteSchema
from rest_framework.permissions import IsAuthenticated
from urbvan_framework.authentication import CustomTokenAuthentication
from urbvan_framework.views import IsStaffUser, IsAnonymousUser, IsSuperUser

"""
Lines CRUD views
 - List
 - Retrive
 - Create
 - Delete
"""

#TODO: Give permissions per view
class LineModelListView(ListAPIView):

    authentication_classes = (CustomTokenAuthentication,)
    permission_classes = (IsAnonymousUser,)

    queryset = LineModel.objects.all()
    schema_class = LinesSchema
    serializer_class = LineModelSerializer


class LineModelDetailView(RetrieveAPIView):

    authentication_classes = (CustomTokenAuthentication,)
    permission_classes = (
        IsAuthenticated,
        IsStaffUser,
    )

    queryset = LineModel.objects.all()
    schema_class = LinesSchema
    serializer_class = LineModelSerializer


class LineModelCreateView(CreateAPIView):

    authentication_classes = (CustomTokenAuthentication,)
    permission_classes = (
        IsAuthenticated,
        IsSuperUser,
    )

    serializer_class = LineModelSerializer
    schema_class = LinesSchema


class LineModelDeleteView(DestroyAPIView):

    authentication_classes = (CustomTokenAuthentication,)
    permission_classes = (IsAuthenticated, IsSuperUser)

    queryset = LineModel.objects.all()
    schema_class = LinesSchema
    serializer_class = LineModelSerializer


"""
 Route CRUD views
 - List
 - Retrive
 - Create
 - Delete
"""
#TODO: Give permissions per view

class RouteModelListView(ListAPIView):

    authentication_classes = (CustomTokenAuthentication,)
    # permission_classes = IsAnonymousUser

    queryset = RouteModel.objects.all()
    schema_class = RouteSchema
    serializer_class = RouteModelSerializer


class RouteModelDetailView(RetrieveAPIView):

    authentication_classes = (CustomTokenAuthentication,)
    # permission_classes = IsAuthenticated

    queryset = RouteModel.objects.all()
    schema_class = RouteSchema
    serializer_class = RouteModelSerializer


class RouteModelCreateView(CreateAPIView):

    authentication_classes = (CustomTokenAuthentication,)
    # permission_classes = IsAuthenticated

    serializer_class = RouteModelSerializer
    schema_class = RouteSchema


class RouteModelDeleteView(DestroyAPIView):

    authentication_classes = (CustomTokenAuthentication,)
    # permission_classes = IsAuthenticated

    queryset = RouteModel.objects.all()
    schema_class = RouteSchema
    serializer_class = RouteModelSerializer

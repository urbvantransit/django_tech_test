from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveAPIView, DestroyAPIView
from apps.lines.models import LineModel, RouteModel
from .serializers import LineModelSerializer, RouteModelSerializer
from .schemas import LinesSchema, RouteSchema
from rest_framework.permissions import IsAuthenticated
from urbvan_framework.authentication import CustomTokenAuthentication


class LineModelListView(ListAPIView):
    """
    Provides a get method handler.
    """
    #authentication_classes = (CustomTokenAuthentication,)
    #permission_classes = (IsAuthenticated,)

    queryset = LineModel.objects.all()
    schema_class = LinesSchema
    serializer_class = LineModelSerializer


class LineModelDetailView(RetrieveAPIView):
    """
    Provides a get method handler.
    """
    #authentication_classes = (CustomTokenAuthentication,)
    #permission_classes = (IsAuthenticated,)

    queryset = LineModel.objects.all()
    schema_class = LinesSchema
    serializer_class = LineModelSerializer



class LineModelCreateView(CreateAPIView):
    """
    Provides a get method handler.
    """
   # authentication_classes = (CustomTokenAuthentication,)
   # permission_classes = (IsAuthenticated,)

    serializer_class = LineModelSerializer
    schema_class = LinesSchema


class LineModelDeleteView(DestroyAPIView):
    """
    Provides a get method handler.
    """
    # authentication_classes = (CustomTokenAuthentication,)
    # permission_classes = (IsAuthenticated,)

    queryset = LineModel.objects.all()
    schema_class = LinesSchema
    serializer_class = LineModelSerializer


"""
 Route CRUD
"""

class RouteModelListView(ListAPIView):
    """
    Provides a get method handler.
    """
    #authentication_classes = (CustomTokenAuthentication,)
    #permission_classes = (IsAuthenticated,)

    queryset = RouteModel.objects.all()
    schema_class = RouteSchema
    serializer_class = RouteModelSerializer


class RouteModelDetailView(RetrieveAPIView):
    """
    Provides a get method handler.
    """
    #authentication_classes = (CustomTokenAuthentication,)
    #permission_classes = (IsAuthenticated,)

    queryset = RouteModel.objects.all()
    schema_class = RouteSchema
    serializer_class = RouteModelSerializer



class RouteModelCreateView(CreateAPIView):
    """
    Provides a get method handler.
    """
   # authentication_classes = (CustomTokenAuthentication,)
   # permission_classes = (IsAuthenticated,)

    serializer_class = RouteModelSerializer
    schema_class = RouteSchema


class RouteModelDeleteView(DestroyAPIView):
    """
    Provides a get method handler.
    """
    # authentication_classes = (CustomTokenAuthentication,)
    # permission_classes = (IsAuthenticated,)

    queryset = RouteModel.objects.all()
    schema_class = RouteSchema
    serializer_class = RouteModelSerializer

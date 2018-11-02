from urbvan_framework.views import ListCreateView,\
                                                       UpdateView,\
                                                       DestroyView,\
                                                       ListAPIView,\
                                                       CreateAPIView

from .schemas import LineSchema, RouteSchema
from .serializers import LineSerializer, RouteSerializer

from .models import LineModel, RouteModel
from ..users.permissions import BasicUser, StaffUser, SuperUser


class LineView(ListCreateView):

    queryset = LineModel.objects.order_by('id').all()
    schema_class = LineSchema
    serializer_class = LineSerializer
    permission_classes = (StaffUser, )


class LineUpdateView(UpdateView):

    queryset = LineModel.objects.all()
    schema_class = LineSchema
    serializer_class = LineSerializer
    permission_classes = (StaffUser, )


class LineDestroyView(DestroyView):
    queryset = LineModel.objects.all()
    schema_class = LineSchema
    serializer_class = LineSerializer
    permission_classes = (SuperUser, )


class RouteListView(ListAPIView):

    queryset = RouteModel.objects.order_by('id').all()
    schema_class = RouteSchema
    serializer_class = RouteSerializer
    permission_classes = (BasicUser, )


class RouteCreateView(CreateAPIView):

    queryset = RouteModel.objects.order_by('id').all()
    schema_class = RouteSchema
    serializer_class = RouteSerializer
    permission_classes = (StaffUser, )


class RouteUpdateView(UpdateView):

    queryset = RouteModel.objects.all()
    schema_class = RouteSchema
    serializer_class = RouteSerializer
    permission_classes = (StaffUser, )


class RouteDestroyView(DestroyView):

    queryset = RouteModel.objects.all()
    schema_class = RouteSchema
    serializer_class = RouteSerializer
    permission_classes = (SuperUser, )

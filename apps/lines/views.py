from urbvan_framework.views import ListCreateView,\
                                                       UpdateView,\
                                                       DestroyView,\
                                                       ListAPIView

from .schemas import LineSchema, RouterSchema
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


class RouterView(ListAPIView):

    queryset = RouteModel.objects.order_by('id').all()
    schema_class = RouterSchema
    serializer_class = RouteSerializer
    permission_classes = (BasicUser, )

from urbvan_framework.views import ListCreateView,UpdateView,DestroyView

from .schemas import LineSchema,RouteSchema
from .serializers import LineSerializer,RouteSerializer
from .models import LineModel,RouteModel
from ..users.permissions import IsAdminUser,IsSuperAdminUser,IsNormalUser

class LineView(ListCreateView):
    queryset = LineModel.objects.all()
    schema_class = LineSchema
    serializer_class = LineSerializer
    permission_classes = (IsNormalUser,)

class LineUpdateView(UpdateView):
    queryset = LineModel.objects.all()
    schema_class = LineSchema
    serializer_class = LineSerializer
    permission_classes = (IsAdminUser,)

class LineDestroyView(DestroyView):
    queryset = LineModel.objects.all()
    schema_class = LineSchema
    serializer_class = LineSerializer
    permission_classes = (IsSuperAdminUser,)

class RouteView(ListCreateView):
    queryset = RouteModel.objects.all()
    schema_class = RouteSchema
    serializer_class = RouteSerializer
    permission_classes = (IsNormalUser,)


class RouteUpdateView(UpdateView):
    queryset = RouteModel.objects.all()
    schema_class = RouteSchema
    serializer_class = RouteSerializer
    permission_classes = (IsAdminUser,)


class RouteDestroyView(DestroyView):
    queryset = RouteModel.objects.all()
    schema_class = RouteSchema
    serializer_class = RouteSerializer
    permission_classes = (IsSuperAdminUser,)

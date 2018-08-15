from urbvan_framework.views import ListCreateView,UpdateView,DestroyView

from .schemas import LineSchema,RouteSchema
from .serializers import LineSerializer,RouteSerializer
from .models import LineModel,RouteModel


class LineView(ListCreateView):
    queryset = LineModel.objects.all()
    schema_class = LineSchema
    serializer_class = LineSerializer

class LineUpdateView(UpdateView):
    queryset = LineModel.objects.all()
    schema_class = LineSchema
    serializer_class = LineSerializer

class LineDestroyView(DestroyView):
    queryset = LineModel.objects.all()
    schema_class = LineSchema
    serializer_class = LineSerializer

class RouteView(ListCreateView):
    queryset = RouteModel.objects.all()
    schema_class = RouteSchema
    serializer_class = RouteSerializer

class RouteUpdateView(UpdateView):
    queryset = RouteModel.objects.all()
    schema_class = RouteSchema
    serializer_class = RouteSerializer

class RouteDestroyView(DestroyView):
    queryset = RouteModel.objects.all()
    schema_class = RouteSchema
    serializer_class = RouteSerializer
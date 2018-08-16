from urbvan_framework.views import ListCreateView,UpdateView,DestroyView

from .schemas import LineSchema,RouteSchema
from .serializers import LineSerializer,RouteSerializer
from .models import LineModel,RouteModel
from ..users.permissions import IsAdminUser,IsSuperAdminUser,IsNormalUser

"""
Views related to :model:`lines.LineModel` and
:model:`lines.RouteModel`.
"""
class LineView(ListCreateView):
    """
    GET and POST for :model:`lines.LineModel`
    child of ListCreateView related to Urbvan 
    Framework.

    **Context**

    ``queryset``
        Queryset of all :model:`lines.LineModel` objects
    ``schema_class``
        Schema of :model:`lines.LineModel`
    ``serializer_class``
        Serializer of :model:`lines.LineModel`
    ``permission_classes``
        Permission classes for get an post :model:`lines.LineModel`
    """
    queryset = LineModel.objects.get_queryset().order_by('id')
    schema_class = LineSchema
    serializer_class = LineSerializer
    permission_classes = (IsNormalUser,)

class LineUpdateView(UpdateView):
    """
    Update :model:`lines.LineModel`
    child of UpdateView related to Urbvan 
    Framework.

    **Context**

    ``queryset``
        Queryset of all :model:`lines.LineModel` objects
    ``schema_class``
        Schema of :model:`lines.LineModel`
    ``serializer_class``
        Serializer of :model:`lines.LineModel`
    ``permission_classes``
        Permission classes for update  :model:`lines.LineModel`
    """
    queryset = LineModel.objects.all()
    schema_class = LineSchema
    serializer_class = LineSerializer
    permission_classes = (IsAdminUser,)

class LineDestroyView(DestroyView):
    """
    Delete :model:`lines.LineModel`
    child of UpdateView related to Urbvan 
    Framework.

    **Context**

    ``queryset``
        Queryset of all :model:`lines.LineModel` objects
    ``schema_class``
        Schema of :model:`lines.LineModel`
    ``serializer_class``
        Serializer of :model:`lines.LineModel`
    ``permission_classes``
        Permission classes for delete a :model:`lines.LineModel`
    """
    queryset = LineModel.objects.all()
    schema_class = LineSchema
    serializer_class = LineSerializer
    permission_classes = (IsSuperAdminUser,)

class RouteView(ListCreateView):
    """
    GET and POST for :model:`lines.RouteModel`
    child of ListCreateView related to Urbvan 
    Framework.

    **Context**

    ``queryset``
        Queryset of all :model:`lines.RouteModel` objects
    ``schema_class``
        Schema of :model:`lines.RouteModel`
    ``serializer_class``
        Serializer of :model:`lines.RouteModel`
    ``permission_classes``
        Permission classes for get an post :model:`lines.RouteModel`
    """
    queryset = RouteModel.objects.get_queryset().order_by('id')
    schema_class = RouteSchema
    serializer_class = RouteSerializer
    permission_classes = (IsNormalUser,)


class RouteUpdateView(UpdateView):
    """
    Update :model:`lines.RouteModel`
    child of UpdateView related to Urbvan 
    Framework.

    **Context**

    ``queryset``
        Queryset of all :model:`lines.RouteModel` objects
    ``schema_class``
        Schema of :model:`lines.RouteModel`
    ``serializer_class``
        Serializer of :model:`lines.RouteModel`
    ``permission_classes``
        Permission classes for update  :model:`lines.RouteModel`
    """
    queryset = RouteModel.objects.all()
    schema_class = RouteSchema
    serializer_class = RouteSerializer
    permission_classes = (IsAdminUser,)


class RouteDestroyView(DestroyView):
    """
    Delete :model:`lines.RouteModel`
    child of UpdateView related to Urbvan 
    Framework.

    **Context**

    ``queryset``
        Queryset of all :model:`lines.RouteModel` objects
    ``schema_class``
        Schema of :model:`lines.RouteModel`
    ``serializer_class``
        Serializer of :model:`lines.RouteModel`
    ``permission_classes``
        Permission classes for delete a :model:`lines.RouteModel`
    """
    queryset = RouteModel.objects.all()
    schema_class = RouteSchema
    serializer_class = RouteSerializer
    permission_classes = (IsSuperAdminUser,)

from rest_framework import viewsets

from apps.lines.models import LineModel
from apps.lines.v1.serializers import LineSerializer
from apps.lines.v1.schemas import LineSchema
from urbvan_framework.views import CRUDLView


class LineViewSet(CRUDLView, viewsets.GenericViewSet):
    queryset = LineModel.objects.all()
    serializer_class = LineSerializer
    schema_class = LineSchema

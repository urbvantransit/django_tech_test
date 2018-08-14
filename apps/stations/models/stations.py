# coding: utf8
from django.db import models

from .locations import LocationModel

from apps.utils import create_id


class StationModel(models.Model):

    id = models.CharField(default=create_id('sta_'), primary_key=True,
                          max_length=30, unique=True)
    location = models.ForeignKey(LocationModel, on_delete=models.DO_NOTHING)
    order = models.IntegerField(default=0)
    is_active = models.BooleanField(default=True)

@api_view(['GET','POST'])
def getAndPostLineModel(request):
    if request.method == 'GET':
        data_promos = LineModel.objects.all()
        data = serializers.serialize('json', data_promos)
        return HttpResponse(data, content_type="application/json")
    if request.method == 'POST':
        serializer = LineSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return HttpResponse(serializer.data,status=status.HTTP_201_CREATED)
        return HttpResponse(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
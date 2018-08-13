from django.shortcuts import render
from rest_framework.decorators import api_view
from django.core import serializers
from django.http import HttpResponse
from .models import LineModel


# Create your views he
@api_view(['GET'])
def getLineModel(request):
    data_promos = LineModel.objects.all()
    print(len(data_promos),type(data_promos))
    data = serializers.serialize('json', data_promos)
    
    return HttpResponse(data, content_type="application/json")
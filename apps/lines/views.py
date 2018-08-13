from django.shortcuts import render
from rest_framework.decorators import api_view
from django.core import serializers
from django.http import HttpResponse
from .models import LineModel
from .serializers import LineSerializer
from rest_framework import status
from rest_framework.response import Response


# Create your views he
@api_view(['GET','POST'])
def getLineModel(request):
    if request.method == 'GET':
        data_promos = LineModel.objects.all()
        print(len(data_promos),type(data_promos))
        data = serializers.serialize('json', data_promos)
        return HttpResponse(data, content_type="application/json")
    if request.method == 'POST':
        serializer = LineSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return HttpResponse(serializer.data,status=status.HTTP_201_CREATED)
        return HttpResponse(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
        

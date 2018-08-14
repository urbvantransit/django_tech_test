from django.shortcuts import render
from rest_framework.decorators import api_view
from django.core import serializers
from django.http import HttpResponse
from .models import LineModel
from .serializers import LineSerializer
from rest_framework import status
from rest_framework.response import Response
import json


# Create your views he
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
        
@api_view(['GET','PUT','DELETE'])
def putAndDeleteLineModel(request,id):
    try:
        line = LineModel.objects.get(pk=id)
    except LineModel.DoesNotExist:
        return HttpResponse(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        print(line.name,line.color)
        data = LineSerializer(line)
        return HttpResponse(json.dumps(data.data))
    if request.method == 'PUT':
        serializer = LineSerializer(line,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return HttpResponse(serializer.data,status=status.HTTP_201_CREATED)
        return HttpResponse(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    if request.method == 'DELETE':
        line.delete()
        return HttpResponse(status=status.HTTP_204_NO_CONTENT)

# coding: utf-8
from django.urls import path

from apps.stations.v1 import views as views_v1

urlpatterns_v1_locations = ([
    path('',
         views_v1.LocationModelViewSet.as_view({
             'get': 'list',
             'post': 'create'
         }),
         name='v1_list_create_location'),
    path('<slug:pk>/',
         views_v1.LocationModelViewSet.as_view({
             'get': 'retrieve',
             'put': 'update',
             'patch': 'partial_update',
             'delete': 'destroy'
         }),
         name='v1_retrieve_update_delete_location')
], 'locations')


urlpatterns_v1_stations = ([
    path('',
         views_v1.StationModelViewSet.as_view({
             'get': 'list',
             'post': 'create'
         }),
         name='v1_list_create_station'),
    path('<slug:pk>/',
         views_v1.StationModelViewSet.as_view({
             'get': 'retrieve',
             'put': 'update',
             'patch': 'partial_update',
             'delete': 'destroy'
         }),
         name='v1_retrieve_update_delete_station')
], 'stations')

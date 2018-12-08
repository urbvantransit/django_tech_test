# coding: utf8
from django.urls import path

from .v1 import views as views_v1

urlpatterns_v1_locations = ([

    path('',
         views_v1.LocationView.as_view(),
         name='v1_list_create_location'),
    path('<pk>',
         views_v1.LocationRUDView.as_view(),
         name='v1_rud_location'),

    path('stations/',
         views_v1.StationView.as_view(),
         name='v1_list_create_station'),
    path('stations/<pk>',
         views_v1.StationRUDView.as_view(),
         name='v1_rud_station'),

], 'locations')

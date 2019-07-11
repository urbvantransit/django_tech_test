# coding: utf8
from django.urls import path

from .v1 import views as views_v1

urlpatterns_v1_locations = ([

    path('',
         views_v1.LocationView.as_view(),
         name='v1_list_create_location'),
    path('<str:pk>', 
        views_v1.LocationDetailView.as_view(),
        name="v1_detail_location")

], 'locations')

urlpatterns_v1_stations = ([

    path('',
         views_v1.StationView.as_view(),
         name='v1_list_create_station'),
    path('<str:pk>', 
        views_v1.StationDetailView.as_view(), 
        name="v1_detail_stations"),

], 'station')

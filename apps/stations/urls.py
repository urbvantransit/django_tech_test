# coding: utf8
from django.urls import path

from .v1 import views as views_v1

urlpatterns_v1_locations = ([

    path('',
         views_v1.LocationListCreateView.as_view(),
         name='v1_list_create_location'),
    path('<str:pk>/', 
    	views_v1.LocationManageView.as_view(), 
    	name='v1_location_manage'),
], 'locations')

urlpatterns_v1_stations = ([

    path('',
         views_v1.StationListCreateView.as_view(),
         name='v1_list_create_station'),
    path('<str:pk>/', 
    	views_v1.StationManageView.as_view(), 
    	name='v1_station_manage'),
], 'stations')

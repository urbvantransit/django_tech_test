# coding: utf8
from django.urls import path

from .v1 import views as views_v1
from .v1.views import RUDLocationAPIView, RUDStationAPIView, StationView

urlpatterns_v1_locations = ([

    path('locations/',
         views_v1.LocationView.as_view(),
         name='v1_list_create_location'),
    path('locations/<str:id>', RUDLocationAPIView.as_view(), name='location_detail'),
    path('stations/', StationView.as_view(), name='list_create_station'),
    path('stations/<str:id>', RUDStationAPIView.as_view(), name='station_detail'),

], 'locations')

# coding: utf8
from django.urls import path

from .v1 import views as views_v1
from .v1.views import StationModelListView, StationModelDetailView, StationModelDeleteView, StationModelCreateView
urlpatterns_v1_locations = ([

    path('', views_v1.LocationView.as_view(), name='v1_list_create_location'),

], 'locations')


urls_stations = ([
    path('stations/', StationModelListView.as_view(), name="stations-all"),
    path('stations/<str:pk>/', StationModelDetailView.as_view(), name="stations-detail"),
    path('stations/create', StationModelCreateView.as_view(), name="stations-create"),
    path('stations/delete/<str:pk>', StationModelDeleteView.as_view(), name="stations-delete"),
], 'stations')

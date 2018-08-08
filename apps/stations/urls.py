# coding: utf8
#DJANGO CORE IMPORTS
from django.urls import path

# URBVAN IMPORTS
from .v1 import views as views_v1


urlpatterns_v1_locations = ([
    path('locations/',views_v1.LocationView.as_view(), name='v1_list_create_location'),  # NOQA
    path('locations/<str:pk>/', views_v1.LocationDetailView.as_view(), name='location-detail'),  # NOQA
    path('stations/', views_v1.StationListView.as_view(), name='stations-list'),  # NOQA
    path('stations/<str:pk>/', views_v1.StationDetailView.as_view(), name='station-detail'),  # NOQA
], 'locations')

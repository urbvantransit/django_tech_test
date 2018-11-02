# coding: utf8
from django.urls import path

from .v1 import views as views_v1

urlpatterns_locations = ([
    path('',
         views_v1.LocationView.as_view(),
         name='locations_list_create'),  # URL to list and create view
    path('<str:pk>/update/',
         views_v1.LocationUpdateView.as_view(),
         name='locations_update'),  # URL to update location
    path('<str:pk>/delete/',
         views_v1.LocationDestroyView.as_view(),
         name='locations_delete')  # URL to delete  location
])

urlpatterns_stations = ([
    path('',
         views_v1.StationListView.as_view(),
         name='stations_list'),
    path('create/',
         views_v1.StationCreateView.as_view(),
         name='stations_list')
])

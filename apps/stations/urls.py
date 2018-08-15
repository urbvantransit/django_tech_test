# coding: utf8
from django.urls import path

from .v1 import views as views_v1

urlpatterns_v1_locations = ([

    path('',views_v1.LocationView.as_view(),
         name='v1_list_create_location'),
    path('<str:pk>/update/',views_v1.LocationUpdateView.as_view(),
         name='v1_update_location'), 
    path('<str:pk>/delete/',views_v1.LocationDestroyView.as_view(),
         name='v1_delete_location'),
    

], 'locations')

urlpatterns_stations = [
    path('',views_v1.StationView.as_view(),
         name='v1_list_create_station'), 
    path('<str:pk>/update/',views_v1.StationUpdateView.as_view(),
         name='v1_update_station'), 
    path('<str:pk>/delete/',views_v1.StationDestroyView.as_view(),
         name='v1_delete_station'), 
]

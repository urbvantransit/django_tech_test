# coding: utf8
from django.urls import path

from .v1 import views as views_v1

urlpatterns_locations = ([
    path('',
         views_v1.LocationView.as_view(),
         name='locations_list_create'),  # URL to list and create view
    path('<str:pk>/update/',
         views_v1.LocationUpdateView.as_view(),
         name='locations_update')  # URL to update line
])

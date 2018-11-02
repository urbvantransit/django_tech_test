# coding: utf8
from django.urls import path

from .views import LocationView


urlpatterns_locations = ([
    path('',
         LocationView.as_view(),
         name='locations_list_create'),  # URL to list and create view
])

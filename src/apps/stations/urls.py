# coding: utf8
from django.urls import path

from .v1 import views as views_v1

urlpatterns_v1_locations = ([
    path(
        '', views_v1.LocationView.as_view(), name='v1_list_location'
    ),
    path(
        '<str:pk>',
        views_v1.LocationDetailView.as_view(),
        name='v1_detail_location'
    )
], 'locations')

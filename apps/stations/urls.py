# coding: utf8
from django.urls import path

from .v1 import views

# Creamos un router y registramos nuestros viewsets para locations
urlpatterns_v1_locations = ([
    # La siguiente url permite solamente GET y POST
    path('', views.LocationView.as_view({
        'get': 'list',
        'post': 'create'
    }), name='v1_list_create_location'),

    # La siguiente url permite solamente GET y PUT, PATCH y DELETE
    path('<str:pk>/', views.LocationView.as_view({
        'get': 'retrieve',
        'put': 'update',
        'patch': 'partial_update',
        'delete': 'destroy'
    }), name='v1_detail_location'),
], 'locations')

# Creamos un router y registramos nuestros viewsets para stations
urlpatterns_v1_stations = ([
    # La siguiente url permite solamente GET y POST
    path('', views.StationView.as_view({
        'get': 'list',
        'post': 'create'
    }), name='v1_list_location'),

    # La siguiente url permite solamente GET y PUT, PATCH y DELETE
    path('<str:pk>/', views.StationView.as_view({
        'get': 'retrieve',
        'put': 'update',
        'patch': 'partial_update',
        'delete': 'destroy'
    }), name='v1_detail_location'),
], 'stations')

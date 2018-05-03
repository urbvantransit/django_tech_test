# coding: utf8
from django.urls import path
from django.contrib.auth.decorators import login_required, permission_required
from .views import LocationListView, LocationCreateView, LocationUpdateView, LocationDeleteView, StationListView, StationCreateView, StationUpdateView, StationDeleteView

urlpatterns_locations = ([

    path('', login_required(LocationListView.as_view()), name='list'),
    path('create', login_required(LocationCreateView.as_view()), name='create'),
    path('update/<str:pk>/', login_required(LocationUpdateView.as_view()), name='update'),
    path('delete/<str:pk>/', login_required(LocationDeleteView.as_view()), name='delete'),

], 'locations')

urlpatterns_stations = ([

    path('', login_required(StationListView.as_view()), name='list'),
    path('create', login_required(StationCreateView.as_view()), name='create'),
    path('update/<str:pk>/', login_required(StationUpdateView.as_view()), name='update'),
    path('delete/<str:pk>/', login_required(StationDeleteView.as_view()), name='delete'),

], 'stations')
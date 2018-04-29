# coding: utf8
from django.urls import path
from .views import LocationListView, LocationCreateView, LocationUpdateView, LocationDeleteView

urlpatterns_v1_locations = ([

    path('', LocationListView.as_view(), name='list'),
    path('create', LocationCreateView.as_view(), name='create'),
    path('update/<str:pk>/', LocationUpdateView.as_view(), name='update'),
    path('delete/<str:pk>/', LocationDeleteView.as_view(), name='delete'),

], 'locations')

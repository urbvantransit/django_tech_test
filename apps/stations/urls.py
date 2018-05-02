# coding: utf8
from django.urls import path
from django.contrib.auth.decorators import login_required, permission_required
from .views import LocationListView, LocationCreateView, LocationUpdateView, LocationDeleteView

urlpatterns_locations = ([

    path('', login_required(LocationListView.as_view()), name='list'),
    path('create', login_required(LocationCreateView.as_view()), name='create'),
    path('update/<str:pk>/', login_required(LocationUpdateView.as_view()), name='update'),
    path('delete/<str:pk>/', login_required(LocationDeleteView.as_view()), name='delete'),

], 'locations')

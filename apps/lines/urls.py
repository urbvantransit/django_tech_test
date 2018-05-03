# coding: utf8
from django.urls import path
from django.contrib.auth.decorators import login_required, permission_required
from .views import LineListView, LineCreateView, LineUpdateView, LineDeleteView, RouteListView, RouteCreateView, RouteUpdateView, RouteDeleteView

urlpatterns_lines = ([

    path('', login_required(LineListView.as_view()), name='list'),
    path('create', login_required(LineCreateView.as_view()), name='create'),
    path('update/<str:pk>/', login_required(LineUpdateView.as_view()), name='update'),
    path('delete/<str:pk>/', login_required(LineDeleteView.as_view()), name='delete'),

], 'lines')

urlpatterns_routes = ([

    path('', login_required(RouteListView.as_view()), name='list'),
    path('create', login_required(RouteCreateView.as_view()), name='create'),
    path('update/<str:pk>/', login_required(RouteUpdateView.as_view()), name='update'),
    path('delete/<str:pk>/', login_required(RouteDeleteView.as_view()), name='delete'),

], 'routes')
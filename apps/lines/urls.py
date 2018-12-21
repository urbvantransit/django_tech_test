# coding: utf8
from django.urls import path
from .v1.views import (LineModelListView, LineModelDetailView, LineModelCreateView, LineModelDeleteView,
                       RouteModelDetailView, RouteModelListView, RouteModelCreateView, RouteModelDeleteView)

urlpatterns = [
    path('lines/', LineModelListView.as_view(), name="line-all"),
    path('lines/<str:pk>/', LineModelDetailView.as_view(), name="line-detail"),
    path('lines/create', LineModelCreateView.as_view(), name="line-create"),
    path('lines/delete/<str:pk>', LineModelDeleteView.as_view(), name="line-delete"),

    path('routes/', RouteModelListView.as_view(), name="routes-all"),
    path('routes/<str:pk>/', RouteModelDetailView.as_view(), name="routes-detail"),
    path('routes/create', RouteModelCreateView.as_view(), name="routes-create"),
    path('routes/delete/<str:pk>', RouteModelDeleteView.as_view(), name="routes-delete"),
]



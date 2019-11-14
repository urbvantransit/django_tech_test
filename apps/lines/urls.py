# coding: utf8
from django.urls import path
from .v1.views import (
    LineModelListView,
    LineModelDetailView,
    LineModelCreateView,
    LineModelDeleteView,
    RouteModelDetailView,
    RouteModelListView,
    RouteModelCreateView,
    RouteModelDeleteView,
)

urlpatterns_lines = [
    path("", LineModelListView.as_view(), name="line-all"),
    path("<str:pk>/", LineModelDetailView.as_view(), name="line-detail"),
    path("create", LineModelCreateView.as_view(), name="line-create"),
    path("lines/delete/<str:pk>", LineModelDeleteView.as_view(), name="line-delete"),
]


urlpatterns_routes = [
    path("", RouteModelListView.as_view(), name="routes-all"),
    path("<str:pk>/", RouteModelDetailView.as_view(), name="routes-detail"),
    path("create", RouteModelCreateView.as_view(), name="routes-create"),
    path("delete/<str:pk>", RouteModelDeleteView.as_view(), name="routes-delete"),
]

# coding: utf8
from django.urls import path
from .v1.views import (
    LineModelListView,
    LineModelDetailView,
    LineModelCreateView,
    LineModelDeleteView,
)

urlpatterns_lines = [
    path("", LineModelListView.as_view(), name="line-all"),
    path("<str:pk>/", LineModelDetailView.as_view(), name="line-detail"),
    path("create", LineModelCreateView.as_view(), name="line-create"),
    path("lines/delete/<str:pk>", LineModelDeleteView.as_view(), name="line-delete"),
]

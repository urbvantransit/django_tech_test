# coding: utf8
from rest_framework.routers import SimpleRouter

from . import views

v1_router = SimpleRouter()
v1_router.register('line', views.LineViewSet)
v1_router.register('route', views.RouteViewSet)
urlpatterns_v1_lines = v1_router.urls

# coding: utf8
from rest_framework.routers import SimpleRouter

from .v1 import views as views_v1

v1_router = SimpleRouter()
v1_router.register('location', views_v1.LocationViewSet)
v1_router.register('station', views_v1.StationViewSet)
urlpatterns_v1_locations = v1_router.urls

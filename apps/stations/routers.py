from rest_framework import routers

from .v1 import views

read_router = routers.DefaultRouter()
write_router = routers.DefaultRouter()

# Stations
read_router.register(r'stations', views.StationReadViewSet)
write_router.register(r'stations', views.StationWriteViewSet)

# Locations
read_router.register(r'locations', views.LocationReadViewSet)
write_router.register(r'locations', views.LocationWriteViewSet)

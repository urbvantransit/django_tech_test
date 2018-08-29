# coding: utf8
from apps.stations.v1 import views as stations_views
from rest_framework import routers
#
router = routers.SimpleRouter()
router.trailing_slash = '/?'
router.register(r'v1/station', stations_views.StationViewSet, base_name='v1_station')
router.register(r'v1/location', stations_views.LocationViewSet, base_name='v1_location')

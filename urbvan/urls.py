from django.contrib import admin
from django.urls import (include, path)
from rest_framework import routers
from rest_framework.authtoken import views

from apps.stations.v1 import views as station_views_v1
from apps.lines.v1 import views as lines_views_v1

read_only_router = routers.DefaultRouter()
read_only_router.register(r'locations', station_views_v1.ReadOnlyLocationViewSet, base_name='read-locations')
read_only_router.register(r'stations', station_views_v1.ReadOnlyStationViewSet, base_name='read-stations')
read_only_router.register(r'lines', lines_views_v1.ReadOnlyLineViewSet, base_name='read-lines')
read_only_router.register(r'routes', lines_views_v1.ReadOnlyRouteViewSet, base_name='read-routes')

write_only_router = routers.DefaultRouter()
write_only_router.register(r'locations', station_views_v1.WriteOnlyLocationViewSet, base_name='write-locations')
write_only_router.register(r'stations', station_views_v1.WriteOnlyStationViewSet, base_name='write-stations')
write_only_router.register(r'lines', lines_views_v1.WriteOnlyLineViewSet, base_name='write-lines')
write_only_router.register(r'routes', lines_views_v1.WriteOnlyRouteViewSet, base_name='write-routes')


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-token-auth/', views.obtain_auth_token),

    path('v1/', include(read_only_router.urls)),
    path('v1/w/', include(write_only_router.urls)),
]

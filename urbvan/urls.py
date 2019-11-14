# coding: utf8
from django.contrib import admin
from django.urls import include, path

from rest_framework.authtoken import views
from apps.stations.urls import urlpatterns_v1_locations, urls_stations
from apps.lines.urls import urlpatterns_routes, urlpatterns_lines

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api-token-auth/", views.obtain_auth_token),
    path("v1/locations/", include(urlpatterns_v1_locations), name="locations"),
    path("v1/stations/", include(urls_stations), name="stations"),
    path("v1/lines/", include(urlpatterns_lines), name="lines"),
    path("v1/routes/", include(urlpatterns_routes), name="routes"),
]

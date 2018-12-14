# coding: utf8
from django.contrib import admin
from django.urls import (include, path)
from rest_framework.authtoken import views
from apps.stations.urls import urlpatterns_v1_locations, urlpatterns_v1_stations
from apps.lines.urls import urlpatterns_v1_lines, urlpatterns_v1_routes
from urbvan_test_frontend import urls as urbvan_test_frontend_urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('api-token-auth/', views.obtain_auth_token),
    # TODO: Implement djoser authentication
    # path('api-auth/', include('djoser.urls')),
    # path('api-auth/', include('djoser.urls.authtoken')),
    # API CRUD URLS
    path('v1/locations/', include(urlpatterns_v1_locations)),
    path('v1/stations/', include(urlpatterns_v1_stations)),
    path('v1/lines/', include(urlpatterns_v1_lines)),
    path('v1/routes/', include(urlpatterns_v1_routes)),
    path('crud/', include(urbvan_test_frontend_urls))
]

# coding: utf8
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import (include, path)

from rest_framework.authtoken import views

from apps.stations.urls import urlpatterns_locations, urlpatterns_stations
from apps.lines.urls import urlpatterns_lines, urlpatterns_routes

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    path('api-token-auth/', views.obtain_auth_token),
    path('locations/', include(urlpatterns_locations)),
    path('stations/', include(urlpatterns_stations)),
    path('lines/', include(urlpatterns_lines)),
    path('routes/', include(urlpatterns_routes)),
    path('', include(urlpatterns_locations)),
]

# coding: utf8
from django.contrib import admin
from django.urls import (include, path)

from rest_framework.authtoken import views

from apps.stations.urls import urlpatterns_v1_locations,urlpatterns_stations
from apps.lines.urls import urlpatterns

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-token-auth/', views.obtain_auth_token),
    path('v1/locations/', include(urlpatterns_v1_locations)),
    path('v1/lines/',include(urlpatterns))
    path('v1/stations/',include(urlpatterns_stations))
]

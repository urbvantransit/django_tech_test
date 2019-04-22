# coding: utf8
from django.contrib import admin
from django.urls import (include, path)

from rest_framework.authtoken import views

from apps.stations.urls import urlpatterns_v1_locations, \
    urlpatterns_v1_stations

from apps.lines.urls import urlpatterns_v1_lines, \
    urlpatterns_v1_routes

from apps.users.urls import urlpatterns_v1_users

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-token-auth/', views.obtain_auth_token),

    path('v1/locations/', include(urlpatterns_v1_locations)),
    path('v1/stations/', include(urlpatterns_v1_stations)),

    path('v1/lines/', include(urlpatterns_v1_lines)),
    path('v1/routes/', include(urlpatterns_v1_routes)),

    path('v1/users/', include(urlpatterns_v1_users),
    )
]

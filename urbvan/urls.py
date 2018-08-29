# coding: utf8
from django.contrib import admin
from django.urls import (include, path)

from django.conf.urls import url

from rest_framework.authtoken import views

from apps.stations.urls import router as station_router
from apps.lines.urls import router as line_router
from apps.users.urls import router as user_router

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-token-auth/', views.obtain_auth_token),
    url(r'', include(station_router.urls)),
    url(r'', include(line_router.urls)),
    url(r'', include(user_router.urls)),
]



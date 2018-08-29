# coding: utf8
from django.contrib import admin
from django.urls import (include, path)

from django.conf.urls import url

from rest_framework.authtoken import views

from apps.stations.urls import router as station_router

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-token-auth/', views.obtain_auth_token),
    url(r'', include(station_router.urls)),
]



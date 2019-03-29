# coding: utf8
from apps.stations.urls import urlpatterns_v1_locations

from django.contrib import admin
from django.urls import (include, path)

from rest_framework.authtoken import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-token-auth/', views.obtain_auth_token),
    path('v1/locations/', include(urlpatterns_v1_locations))
]

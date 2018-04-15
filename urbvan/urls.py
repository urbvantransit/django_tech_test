# coding: utf8
from django.contrib import admin
from django.urls import (include, path)

from rest_framework.authtoken import views

from apps.stations.urls import urlpatterns_v1_locations

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-token-auth/', views.obtain_auth_token),

    path('v1/locations/', include(urlpatterns_v1_locations))
]

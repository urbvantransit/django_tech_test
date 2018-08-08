# coding: utf8
# DJANGO CORE IMPORTS
from django.contrib import admin
from django.urls import (include, path)

# THIRD-PARTY IMPORTS
from rest_framework.authtoken import views

# URBVAN IMPORTS
from apps.stations.urls import urlpatterns_v1_locations
from apps.lines.urls import lines_app_router

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-token-auth/', views.obtain_auth_token),
    path('v1/', include(urlpatterns_v1_locations)),
    path('v1/', include(lines_app_router.urls)),
]

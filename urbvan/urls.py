# coding: utf8
from django.contrib import admin
from django.urls import include, path
from rest_framework.authtoken import views

from apps.stations.urls import urlpatterns_v1_locations

urlpatterns = [
    path('admin/', admin.site.urls),
    # URLS de DRF auth token
    path('api-token-auth/', views.obtain_auth_token),
    # URLs de apps
    path('v1/', include(urlpatterns_v1_locations)),
    path('v1/', include('apps.lines.urls')),
    # URLs de app users
    path('v1/accounts/', include('apps.users.urls')),
]

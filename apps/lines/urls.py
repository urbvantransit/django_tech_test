from django.urls import path

from apps.lines.views import (
    ListCreateLineAPIView, ListCreateRouteAPIView,
    RetrieveUpdateDestroyAPIView, RetrieveUpdateDestroyRouteAPIView)

app_name = 'lines_routes'

urlpatterns = [
    path('lines/', ListCreateLineAPIView.as_view(), name='list_create_line'),
    path('lines/<str:id>', RetrieveUpdateDestroyAPIView.as_view(), name='lines_detail'),
    # URLs de RouteModel
    path('routes/', ListCreateRouteAPIView.as_view(), name='list_create_route'),
    path('routes/<str:id>', RetrieveUpdateDestroyRouteAPIView.as_view(), name='routes_detail'),
]

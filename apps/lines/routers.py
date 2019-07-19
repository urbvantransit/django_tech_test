from rest_framework import routers

from .v1 import views

read_router = routers.DefaultRouter()
write_router = routers.DefaultRouter()

# Lines
read_router.register(r'lines', views.LineReadViewSet)
write_router.register(r'lines', views.LineWriteViewSet)

# Routes
read_router.register(r'routes', views.RouteReadViewSet)
write_router.register(r'routes', views.RouteWriteViewSet)

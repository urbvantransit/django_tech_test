# THIRD-PARTY IMPORTS
from rest_framework import routers

# URBVAN IMPORTS
from .api.viewsets import (
    LineModelViewset,
    RouteModelViewset,
)

lines_app_router = routers.DefaultRouter()
lines_app_router.register(r'lines', LineModelViewset)
lines_app_router.register(r'routes', RouteModelViewset)

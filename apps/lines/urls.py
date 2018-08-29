# coding: utf8

from apps.lines.v1 import views as lines_views
from rest_framework import routers
#
router = routers.SimpleRouter()
router.trailing_slash = '/?'
router.register(r'v1/line', lines_views.LineViewSet, base_name='v1_line')
router.register(r'v1/route', lines_views.RouteViewSet, base_name='v1_route')

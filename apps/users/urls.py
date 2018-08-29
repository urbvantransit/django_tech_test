# coding: utf8

from apps.users.v1 import views as users_views
from rest_framework import routers
#
router = routers.SimpleRouter()
router.trailing_slash = '/?'
router.register(r'v1/user', users_views.UserViewSet, base_name='v1_user')


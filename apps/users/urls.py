from django.urls import path
from django.conf.urls import url

from .v1 import views as views_v1

urlpatterns_v1_users = ([

    path('',
         views_v1.UserCreateView.as_view(),
         name='v1_user_create'),
    path('<int:pk>/', views_v1.UserManageView.as_view(), name='v1_user_manage'),

], 'users')

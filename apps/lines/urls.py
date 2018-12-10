# coding: utf8
from django.urls import path

from .v1 import views as views_v1

urlpatterns_v1_lines = ([

    path('',
         views_v1.LineView.as_view(),
         name='v1_list_create_line'),
    path('<pk>',
         views_v1.LineRUDView.as_view(),
         name='v1_rud_line'),

    path('routes/',
         views_v1.RouteView.as_view(),
         name='v1_list_create_route'),
    path('routes/<pk>',
         views_v1.RouteRUDView.as_view(),
         name='v1_rud_route'),

], 'lines')

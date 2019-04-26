# coding: utf-8
from django.urls import path

from apps.lines.v1 import views as views_v1

urlpatterns_v1_lines = ([
    path('',
         views_v1.LineListCreateView.as_view(),
         name='v1_list_create_line'),
    path('<slug:pk>/',
         views_v1.LineRetrieveUpdateDeleteView.as_view(),
         name='v1_retrieve_update_delete_line')
], 'lines')


urlpatterns_v1_routes = ([
    path('',
         views_v1.RouteListCreateView.as_view(),
         name='v1_list_create_route'),
    path('<slug:pk>/',
         views_v1.RouteRetrieveUpdateDeleteView.as_view(),
         name='v1_retrieve_update_delete_route')
], 'routes')

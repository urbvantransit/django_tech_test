# coding: utf-8
from django.urls import path

from apps.lines.v1 import views as views_v1

urlpatterns_v1_lines = ([
    path('',
         views_v1.LineModelViewSet.as_view({
             'get': 'list',
             'post': 'create'
         }),
         name='v1_list_create_line'),
    path('<slug:pk>/',
         views_v1.LineModelViewSet.as_view({
             'get': 'retrieve',
             'put': 'update',
             'patch': 'partial_update',
             'delete': 'destroy'
         }),
         name='v1_retrieve_update_delete_line')
], 'lines')


urlpatterns_v1_routes = ([
    path('',
         views_v1.RouteModelViewSet.as_view({
             'get': 'list',
             'post': 'create'
         }),
         name='v1_list_create_route'),
    path('<slug:pk>/',
         views_v1.RouteModelViewSet.as_view({
             'get': 'retrieve',
             'put': 'update',
             'patch': 'partial_update',
             'delete': 'destroy'
         }),
         name='v1_retrieve_update_delete_route')
], 'routes')

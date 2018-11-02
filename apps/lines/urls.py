# coding: utf8
from django.urls import path

from .views import LineView,\
                            LineUpdateView,\
                            LineDestroyView,\
                            RouteListView,\
                            RouteCreateView,\
                            RouteUpdateView,\
                            RouteDestroyView


urlpatterns_lines = ([

    path('',
         LineView.as_view(),
         name='line_list'),  # URL to list and create view
    path('<str:pk>/update/',
         LineUpdateView.as_view(),
         name='line_update'),  # URL to update line
    path('<str:pk>/delete/',
         LineDestroyView.as_view(),
         name='line_delete')  # URL to delete line

], 'lines')

urlpatterns_routes = ([
    path('',
         RouteListView.as_view(),  # URL to list routes
         name='route_list'),
    path('create/',
         RouteCreateView.as_view(),
         name='route_creat'),  # URL to create routes
    path('<str:pk>/update/',
         RouteUpdateView.as_view(),
         name='route_update'),  # URL to update routes
    path('<str:pk>/delete/',
         RouteDestroyView.as_view(),  # URL to delete routes
         name='route')
], 'routes')

# created by victor p - 16/12/2018
from django.urls import path
from .v1 import views as views_v1

urlpatterns_v1_lines = ([
    path('',
         views_v1.LineView.as_view(),
         name='v1_list_create_line'),
    path('<str:pk>',
         views_v1.LineDetailView.as_view(),
         name='v1_detail_line'),

    ], 'lines')

urlpatterns_v1_routes = ([
    path('',
         views_v1.RouteView.as_view(),
         name='v1_list_create_route'),
    path('<str:pk>',
      views_v1.RouteDetailView.as_view(),
      name='v1_detail_route'),
    ], 'routes')
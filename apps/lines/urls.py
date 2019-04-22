from django.urls import path

from .v1 import views as views_v1

urlpatterns_v1_lines = ([

    path('',
         views_v1.LineListCreateView.as_view(),
         name='v1_list_create_line'),
    path('<str:pk>/', 
    	views_v1.LineManageView.as_view(), 
    	name='v1_line_manage'),
], 'lines')

urlpatterns_v1_routes = ([

    path('',
         views_v1.RouteListCreateView.as_view(),
         name='v1_list_create_route'),
    path('<str:pk>/', 
    	views_v1.RouteManageView.as_view(), 
    	name='v1_route_manage'),
], 'routes')
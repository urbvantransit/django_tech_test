# coding: utf8
from django.urls import path

from .v1 import views as views_v1

urlpatterns_v1_locations = ([

    path('',views_v1.LocationView.as_view(),
         name='v1_list_create_location'),

], 'locations')

urlpatterns_stations = [
    path('',views_v1.getAndPostLineModel),
    path('<str:id>',putAndDeleteLineModel),
    # path('index/', views.index, name='main-view'),
    # path('menu/', views.menu, name='menu-view'),
    # path('list/', views.layout_list, name='list-view'),
    # path('promos_list/', views.promos_list, name='promos-view'),
    # path('stores/<str:search>', views.get_stores, name='stores-view'),

]

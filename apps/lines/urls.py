from django.urls import path

from .views import getAndPostLineModel,putAndDeleteLineModel


urlpatterns = [
    path('',getAndPostLineModel),
    path('<str:id>',putAndDeleteLineModel),
    # path('index/', views.index, name='main-view'),
    # path('menu/', views.menu, name='menu-view'),
    # path('list/', views.layout_list, name='list-view'),
    # path('promos_list/', views.promos_list, name='promos-view'),
    # path('stores/<str:search>', views.get_stores, name='stores-view'),

]
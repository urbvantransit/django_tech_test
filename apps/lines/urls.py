from django.urls import path

from . import views


urlpatterns = [
    path('', views.getLineModel),
    # path('index/', views.index, name='main-view'),
    # path('menu/', views.menu, name='menu-view'),
    # path('list/', views.layout_list, name='list-view'),
    # path('promos_list/', views.promos_list, name='promos-view'),
    # path('stores/<str:search>', views.get_stores, name='stores-view'),

]
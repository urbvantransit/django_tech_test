from django.urls import path

from .views import (LineView,LineUpdateView,LineDestroyView,
                    RouteView,RouteUpdateView,RouteDestroyView)


urlpatterns_line = [
    path('',LineView.as_view(),
         name='v1_list_create_Line'), 
    path('<str:pk>/update',LineUpdateView.as_view(),
         name='v1_update_Line'), 
    path('<str:pk>/',LineDestroyView.as_view(),
         name='v1_delete_Line'),
]

urlpatterns_route = [
    path('',RouteView.as_view(),
         name='v1_list_create_route'), 
    path('<str:pk>/update/',RouteUpdateView.as_view(),
         name='v1_update_Route'), 
    path('<str:pk>/',RouteDestroyView.as_view(),
         name='v1_delete_Route'),
]
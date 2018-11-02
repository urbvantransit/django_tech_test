# coding: utf8
from django.urls import path

from .views import LineView, RouterView, LineUpdateView, LineDestroyView

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

])

urlpatterns_router = ([
    path('',
         RouterView.as_view(),  # URL to list routers
         name='router_list')
])

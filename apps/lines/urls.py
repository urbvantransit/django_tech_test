# coding: utf8
from django.urls import path
from .views import LineModelCreate, LineModelDetail, LineModelDelete, LineModelList

urlpatterns = [
    path('create', LineModelCreate.as_view(), name='line_model_create_view'),
    path('update/<str:pk>', LineModelDetail.as_view(), name='line_model_update_view'),
    path('delete/<str:pk>', LineModelDelete.as_view(), name='line_model_delete_view'),
    path('', LineModelList.as_view(), name='line_model_list_view'),

]



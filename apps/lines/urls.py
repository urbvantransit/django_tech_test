
from django.urls import path

from .views import LineView, LineCreateView, LineDetailView, LineUpdateView, LineDeleteView

app_name = "lines"

# app_name will help us do a reverse look-up latter.
urlpatterns = [
    path('', LineView.as_view(), name='lineas'),
    path('/create', LineCreateView.as_view(), name='create'),
    path('/<str:id>', LineDetailView.as_view(), name='detail'),
    path('/<str:pk>/update', LineUpdateView.as_view(), name='update'),
    path('/<str:pk>/delete', LineDeleteView.as_view(), name='delete'),
]
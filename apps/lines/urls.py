
from django.urls import path

from .views import LineView, LineCreateView, LineDetailView, LineUpdateView, LineDeleteView, RouteView

app_name = "lines"

# app_name will help us do a reverse look-up latter.
lines_urlpatterns = ([
    path('', LineView.as_view(), name='lineas'),
    path('create', LineCreateView.as_view(), name='create'),
    path('<str:id>', LineDetailView.as_view(), name='detail'),
    path('<str:pk>/update', LineUpdateView.as_view(), name='update'),
    path('<str:pk>/delete', LineDeleteView.as_view(), name='delete'),
], 'lines')

routes_urlpatterns = ([
    path('', RouteView.as_view(), name='rutas'),
], 'routes')
from django.urls import path
from .views import (
    UsersListView,
    UsersDetailView,
    UsersCreateView,
    HomeView
)

# Create your urls here.
# Add the class in views.py as View
app_name='users'
urlpatterns = [
    path('',HomeView.as_view(), name='user-list'),
    path('lista-de-usuarios',UsersListView.as_view(), name='user-list'),
    path('crear/',UsersCreateView.as_view(),name='user-create'),
    path('<int:id>/',UsersDetailView.as_view(), name='user-detail'),
]

from django.urls import path
from .views import (
    UsersListView,
    UsersDetailView
)

# Create your urls here.
# Add the class in views.py as View
app_name='users'
urlpatterns = [
    path('',UsersListView.as_view(), name='user-list'),
    path('<int:pk>/',UsersDetailView.as_view(), name='user-detail'),
]

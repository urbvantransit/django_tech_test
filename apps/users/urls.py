from django.urls import path

from .views import RegisterUserAPIView

app_name = 'users'

urlpatterns = [
    path('signup/', RegisterUserAPIView.as_view(), name='signup'),
]

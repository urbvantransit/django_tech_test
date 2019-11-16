from django.urls import path
from apps.lines.views import (ListCreateLineView, )

app_name = 'lines'

urlpatterns = [
    path('', ListCreateLineView.as_view(), name='list_create_line'),
]

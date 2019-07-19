from django.urls import (include, path)

from .routers import (read_router, write_router)

urlpatterns = [
    path('/', include(read_router.urls)),
    path('/write/', include(write_router.urls)),
]

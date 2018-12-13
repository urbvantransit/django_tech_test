from django.contrib import admin
from . import models as lines_models

# Registering models to be managed by the Django admin interface
admin.site.register(lines_models.LineModel)
admin.site.register(lines_models.RouteModel)
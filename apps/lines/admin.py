from django.contrib import admin

from . import models

admin.site.register(models.LineModel)
admin.site.register(models.RouteModel)

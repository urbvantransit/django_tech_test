from django.contrib import admin

from apps.stations.models import StationModel
from . import models as lines_models

# Registering models to be managed by the Django admin interface
class StationsInline(admin.StackedInline):
    model = StationModel
    extra = 1
    fk_name = 'route'


class RouteModelAdmin(admin.ModelAdmin):
    save_on_top = True
    inlines = [StationsInline]

admin.site.register(lines_models.LineModel)
admin.site.register(lines_models.RouteModel,RouteModelAdmin)

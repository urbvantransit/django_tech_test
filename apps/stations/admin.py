from django.contrib import admin

from apps.stations.models.locations import LocationModel
from apps.stations.models.stations import StationModel
# Register your models here.

admin.site.register(LocationModel)
admin.site.register(StationModel)
from django.contrib import admin
from . import models as stations_models
# Registering models to be managed by the Django admin interface
admin.site.register(stations_models.locations.LocationModel)
admin.site.register(stations_models.stations.StationModel)
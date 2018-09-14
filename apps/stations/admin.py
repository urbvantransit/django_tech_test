from django.contrib import admin

from . import models


class StationsAppAdmin(admin.ModelAdmin):
    list_display = ('id', '__str__')


admin.site.register(models.LocationModel, StationsAppAdmin)
admin.site.register(models.StationModel, StationsAppAdmin)

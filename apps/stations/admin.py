from django.contrib import admin

from .models import LocationModel, StationModel


class LocationModelAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    search_fields = ('name', 'key')

admin.site.register(LocationModel, LocationModelAdmin)


class StationModelAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'location', 'order', 'is_active')
    search_fields = ('name', 'key')

admin.site.register(StationModel, StationModelAdmin)
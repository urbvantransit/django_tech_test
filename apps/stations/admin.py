from django.contrib import admin
from .models import LocationModel


class LocationModelAdmin(admin.ModelAdmin):
	list_display = ('id','name', 'key', 'created', 'modified', 'active')
	search_fields = ('name', 'key')
	readonly_fields = ('created', 'modified',)
	date_hierarchy = ('created')

admin.site.register(LocationModel, LocationModelAdmin)

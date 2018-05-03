from django.contrib import admin

from .models import LineModel, RouteModel


class LineModelAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    search_fields = ('name', 'key')

admin.site.register(LineModel, LineModelAdmin)


class RouteModelAdmin(admin.ModelAdmin):
    list_display = ('id', 'line', 'direction', 'is_active')
    #search_fields = ('name', 'key')

admin.site.register(RouteModel, RouteModelAdmin)
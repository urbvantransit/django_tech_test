from django.contrib import admin

from .models import LineModel, RouteModel


# Register your models here.
@admin.register(LineModel)
class LineModelAdmin(admin.ModelAdmin):
    

    list_display = ('id', 'name', 'color', )
    ordering = ('id', 'name', 'color', )
    search_fields = ('name', )

# @admin.register(RouteModel)
# class RouteModelAdmin(admin.ModelAdmin):

#     list_display = ('id', 'line', 'station', 'directions', 'is_active', )
#     ordering = ('is_active', )
#     search_fields = ('is_active',)
admin.site.register(RouteModel)

from django.contrib import admin
from apps.stations.models.stations import Historical

# Register your models here.


class HistoricalAdmin(admin.ModelAdmin):
    fields = ("event", "model_type", "created_at", "updated_at")
    readonly_fields = ("created_at", "updated_at")
    list_display = ("event", "model_type", "created_at", "updated_at")


admin.site.register(Historical, HistoricalAdmin)

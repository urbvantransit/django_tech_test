from django.contrib import admin, auth
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import User


class UserAdmin(BaseUserAdmin):
	fieldsets = BaseUserAdmin.fieldsets + (
			('Tiers', {'fields': ('is_tier2','is_tier3')}),
		)

admin.site.unregister(auth.models.Group)
admin.site.register(User, UserAdmin)

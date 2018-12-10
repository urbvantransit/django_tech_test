# coding: utf8

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.forms import UserChangeForm

from .models import User


class UrbvanUserChangeForm(UserChangeForm):

    class Meta(UserChangeForm.Meta):
        model = User


class UrbvanUserAdmin(UserAdmin):

    form = UrbvanUserChangeForm
    list_display = (
    	'user_type', 'email', 'first_name', 'last_name',
    	'is_active', 'date_joined', 'is_staff'
    )
    list_display_links = ('email', )
    list_filter = ('user_type', ) + UserAdmin.list_filter
    fieldsets = (
        (None, {'fields': ('user_type',)}),
    ) + UserAdmin.fieldsets


admin.site.register(User, UrbvanUserAdmin)

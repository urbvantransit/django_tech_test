from django.contrib import admin
from django.contrib.auth.forms import UserChangeForm

from .models import User, UserProfile, DriveProfile

class UserAdmin(admin.ModelAdmin):
    """
    Clase para el Admin en la cual nos permite ver los datos
    del usuario desde el administrador pero, con seguridad, ya que,
    al crear un modelo usuario personzaliado, los campos en el lado
    del admin, quedan vulnerables a una manipulación (en el caso de password)
    de esta manera, se asegura que no se pueda manipular el password.
    Y también otorga que se vea la UI del admin más estética y 
    amigable, como la que tenía originalmente.
    """
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Personal info', {'fields': ('first_name', 'last_name')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser',
                                    'groups', 'user_permissions')}),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
    )
    limited_fieldsets = (
        (None, {'fields': ('email',)}),
        ('Personal info', {'fields': ('first_name', 'last_name')}),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2')
        }),
    )
    form = UserChangeForm
    list_display = ('email', 'first_name', 'last_name', 'is_superuser', 'date_joined')
    list_filter = ('is_staff', 'is_superuser', 'is_active', 'groups', 'date_joined')
    search_fields = ('first_name', 'last_name', 'email')
    ordering = ('email',)
    readonly_fields = ('last_login', 'date_joined',)


class DriverProfileAdmin(admin.ModelAdmin):
    

    list_display = ('id', 'placas', 'unidad', )
    ordering = ('id', 'placas', 'unidad', )
    search_fields = ('placas', 'unidad', )

class UserProfileAdmin(admin.ModelAdmin):

    list_display = ('id', 'address', 'location', )
    ordering = ('location', )

admin.site.register(UserProfile, UserProfileAdmin)
admin.site.register(DriveProfile, DriverProfileAdmin)
admin.site.register(User, UserAdmin)

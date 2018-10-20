from django.contrib import admin

# Register your models here.
# Register the User class as a model to view into admin site
from .models import Users


admin.site.register(Users)

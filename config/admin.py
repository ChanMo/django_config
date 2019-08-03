from django.contrib import admin
from .models import *

class ConfigAdmin(admin.ModelAdmin):
    list_display = ('code', 'value', 'description')
    list_per_page = 10

admin.site.register(Config, ConfigAdmin)

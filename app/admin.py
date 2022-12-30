from django.contrib import admin
from .models import *


class ModelNameAdmin(admin.ModelAdmin):
    list_display = ['field1', 'field2', 'field3']


# Register your models here.
admin.site.register(ModelName, ModelNameAdmin)

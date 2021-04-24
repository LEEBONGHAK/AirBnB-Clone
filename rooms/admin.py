from django.contrib import admin
from . import models

# Register your models here.


@admin.register(models.Room)
class RoonAdmin(admin.ModelAdmin):

    pass
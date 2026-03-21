# Register your models here.
# Модели для администрирования

from django.contrib import admin

from .models import Coords, Pereval, Users

admin.site.register(Coords)
admin.site.register(Pereval)
admin.site.register(Users)

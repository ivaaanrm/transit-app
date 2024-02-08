from django.contrib import admin
from pages.models import Incidencia, Log
# Register your models here.

class IncidenciaAdmin(admin.ModelAdmin):
    pass

class LogAdmin(admin.ModelAdmin):
    pass


admin.site.register(Incidencia, IncidenciaAdmin)

admin.site.register(Log, LogAdmin)

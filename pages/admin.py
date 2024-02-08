from django.contrib import admin
from pages.models import Incidencia
# Register your models here.

class IncidenciaAdmin(admin.ModelAdmin):
    pass


admin.site.register(Incidencia, IncidenciaAdmin)


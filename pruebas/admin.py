from django.contrib import admin
from .models import Prueba 
# Register your models here.


class PruebaAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'subtitulo', 'estado_cantidad')

    search_fields = ('titulo',)

    list_filter = ('activate',)

    def estado_cantidad(self, obj):
        if obj.cantidad > 10:
            return 'Alto stock'
        else:
            return 'Bajo stock'
    
    estado_cantidad.short_description = 'Estado Cantidad'

admin.site.register(Prueba, PruebaAdmin)
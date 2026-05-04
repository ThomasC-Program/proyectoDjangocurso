from django.contrib import admin
from .models import Empleado, Habilidades

# Register your models here.
admin.site.register(Habilidades)


class EmpleadoAdmin(admin.ModelAdmin):
    list_display = (
        'first_name',
        'last_name',
        'departamento',
        'job',
        'full_name',
        'id',
    
    ) #Me permite mostrar en admin el nombre, apellido, departamento, trabajo de manera visual
    
    #
    def full_name(self, obj): # funcion que me permite agregar una columna que no esta relacionada de ninguna forma a mi modelo
        print(obj.first_name) # me permite agregar una columan con valores que yo elija como una suma o algun nombre especial
        return obj.first_name + ' ' + obj.last_name
    #
    
    search_fields = ('last_name',) # Me agrega una barra de busqueda que me permite buscar por lo que quiera en este caso last_name
    list_filter = ('departamento', 'job', 'habilidades',) # En la parte derechea del panel de admin me muestra un flitro por categoria de lo que he especificado

    filter_horizontal = ('habilidades',) #Mejora visual para no tener que depender de una lista sino que con dos cajas puedo mover entre habilidades

admin.site.register(Empleado, EmpleadoAdmin) # T aqui le estoy diciendo que registre Empleadp pero con la configuración que hemos implementado
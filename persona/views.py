from django.shortcuts import render
from django.views.generic import(
    ListView,
    DetailView,
)
# Create your views here.
from .models import Empleado
# Cambios ramaOne 
class ListAllEmpleados(ListView):
    template_name = 'persona/list_all.html'
    paginate_by = 2
    model = Empleado 

class ListByAreaEmpleado(ListView):
    """ lista empleados de un area """
    template_name = 'persona/list_by_area.html'
    
    
    def get_queryset(self):
        area = self.kwargs['shorname']
        lista = Empleado.objects.filter(
            departamento__shor_name=area #Se usa para entrar en una relación en modelo BD
        )
        return lista

class ListByTrabajo(ListView):
    """ lista de empleados por trabajo """
    template_name = 'persona/list_by_trabajo.html'
    
    def get_queryset(self):
        area2 = self.kwargs['job']
        lista = Empleado.objects.filter(
            job=area2 #Se cambia y se usa para cuando solo sea un atributo simple sin relacion alguna
        )
        return lista

class ListEmpleadosByKword(ListView): #
    """ lista empleado por palabra clave """
    template_name = 'persona/by_kword.html'
    context_object_name = 'empleados'
    
    def get_queryset(self):
        palabra_clave = self.request.GET.get("kword", '')
        lista = Empleado.objects.filter(
            first_name = palabra_clave
        )
        
        return lista
    
class ListHabilidadesEmpleado(ListView):
    """ listar las habilidades de los empleados"""
    template_name = 'persona/habilidades.html'
    context_object_name = 'habilidades' #para poder llamar en el html mas facilmente
    
    def get_queryset(self):
        empleado = Empleado.objects.get(id=2 )
        print(empleado.habilidades.all())
        return empleado.habilidades.all()

class EmpleadoDetailView(DetailView):
    model = Empleado
    template_name = "persona/detail_empleado.html"
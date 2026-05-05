from django.shortcuts import render
from django.urls import reverse_lazy # Para redirigir al usuario con mejores practicas paquete de Django
from django.views.generic import(
    ListView, #Importando vistas genéricas
    DetailView,
    CreateView,
    TemplateView,
    UpdateView,
    DeleteView,
)
# Toda vista basada en clases necesita un template para poder funcionar
# Create your views here.
from .models import Empleado

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
    """ Vista para mostrar el detalle de un empleado"""
    model = Empleado
    template_name = "persona/detail_empleado.html"

    def get_context_data(self, **kwargs): #Se define el contexto de la vista
        context = super(EmpleadoDetailView, self).get_context_data(**kwargs) 
        context['titulo'] = 'Empleado del mes'
        return context

class SuccessView(TemplateView): # Template View solo se usa para llamar a un Template Html
    template_name = "persona/success.html"


class EmpleadoCreateView(CreateView):
    model = Empleado
    template_name = "persona/add.html"
    #fields = ('__all__') # Muestra todos los campos del modelo
    fields = [
        'first_name',
        'last_name', 
        'job', 
        'departamento', 
        'habilidades', 
        ] #Muestra cajas de texto para todos los campos del modelo
    success_url = reverse_lazy('persona_app:correcto')
    # Con '.' se le indica a donde debe redirigir al usuario cuando se registra algo
    # Cuando se le pone '.' significa que es al mismo lugar sino colocar '/lista-todo-empleados/'
    #success_url = '.' 
    # Para mejores practicas se usa reverse_lazy como paquete de Django el cual 
    # Redirige al usuario a una URL que debe ser especificada tambien en urls.py del proyecto

    def form_valid(self, form):
        #Interceptar cuando pase algo antes del guardado 
        #En este caso nombre completos
        empleado = form.save(commit=False)
        empleado.full_name = empleado.first_name + ' ' + empleado.last_name
        empleado.save()
        return super(EmpleadoCreateView, self).form_valid(form)

class EmpleadoUpdateView(UpdateView):
    template_name = "persona/update.html"
    model = Empleado
    fields = [
        'first_name',
        'last_name',
        'job',
        'departamento',
        'habilidades',
    ]
    success_url = reverse_lazy('persona_app:correcto')

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        return super().post(request, *args, **kwargs)
    
    def form_valid(self, form):
        #Interceptar cuando pase algo antes del guardado 
        #En este caso nombre completos
        
        return super(EmpleadoUpdateView, self).form_valid(form)

class EmpleadoDeleteView(DeleteView):
    model = Empleado
    template_name = "persona/delete.html"
    success_url = reverse_lazy('persona_app:correcto')
    
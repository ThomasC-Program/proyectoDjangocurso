from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import(
    ListView,
)
from .models import Prueba

class ListPrueba(ListView):
    model = Prueba
    template_name = 'pruebas/list_prueba.html'
    success_url = reverse_lazy('prob_app:lista_prueba')
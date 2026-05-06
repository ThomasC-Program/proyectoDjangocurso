from django.contrib import admin
from django.urls import path

from . import views

app_name = 'home_app'

urlpatterns = [
    path('prueba/', views.PruebaListView.as_view()),
    path('lista/', views.ListarPrueba.as_view()),
    path('lista-prueba/', views.ListarPrueba.as_view()),
    path('add/', views.PruebaCreateView.as_view(), name='prueba_add'),
]
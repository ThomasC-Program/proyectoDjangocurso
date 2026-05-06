from django.urls import path

from . import views

app_name = 'prob_app'

urlpatterns = [
    path(
        'lista-prueba/',
        views.ListPrueba.as_view(),
        name='lista_prueba',
    )
]
from django.db import models

# Create your models here.
class Prueba(models.Model):
    titulo = models.CharField(max_length=100, blank=True)
    subtitulo = models.CharField(max_length=50)
    cantidad = models.IntegerField()
    activate = models.BooleanField(default=True)

    class Meta: 
        verbose_name = 'Prueba'
        verbose_name_plural = 'Lista Prueba' 
        ordering = ['titulo']

    def __str__(self):
        return str(self.id) + '-' + self.titulo + '-' + self.subtitulo + '-' + str(self.cantidad)
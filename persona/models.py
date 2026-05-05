from django.db import models
from departamento.models import Departamento

from django_ckeditor_5.fields import CKEditor5Field

#Para hacer las claves de valor para relacionar tablas se importa la tabla 
# Create your models here.

class Habilidades(models.Model):
    habilidad = models.CharField('Habilidad',max_length=50)
    
    class Meta:
        verbose_name = 'Habilidad'
        verbose_name_plural = 'Habilidad Empleados'
        
    def __str__(self):
        return str(self.id) + '-' + self.habilidad

class Empleado(models.Model):
    """Modelo para tabla empleado"""
    
    #Uso de choices en el código para elejir el job
    JOB_CHOICES = (
        ('0', 'CONTADOR'),
        ('1', 'ADMINISTRADOR'),
        ('2', 'ECONOMISTA'),
        ('3', 'OTRO'),
    )
    
    first_name = models.CharField('Nombres', max_length=60)
    last_name = models.CharField('Apellidos', max_length=60)
    full_name = models.CharField(
        'Nombres Completos',
        max_length=120,
        blank=True
    )

    #(Con choices hacemos que sea elegible el campo)
    job = models.CharField('Trabajo', max_length=50, choices=JOB_CHOICES)
    departamento = models.ForeignKey(Departamento, on_delete=models.CASCADE)
    #ForeignKey para relacionar las tablas es decir de Muchos a Uno 
    #(empleado puede pertenecer a un solo departamento)"Departamento" hace referencia al models.py de departamento
    #on_delete CASCADE sirve para decir que si se borra el Departamento debe borrarse los empleados(este CASCADE se puede cambiar)
    #image = models.ImageField( , upload_to=None, height_field=None, width_field=None, max_length=None)
    habilidades = models.ManyToManyField(Habilidades) #Funcion de muchos a muchos
    #Un empleado puede tener varia habilidades
    #Varias habilidades pueden pertenecer a varios empleados
    hoja_vida = CKEditor5Field('Hoja de Vida', config_name='extends') 

    
    #class Meta va especificando el orden y tratamiento de los datos
    class Meta:
        verbose_name = 'Departamento Empleado' #Cambiar nombre en consultas solo singular
        verbose_name_plural = 'Area del empleado' #Cambiar nombre en plural
        ordering = ['first_name'] + ['last_name'] #Orden del first y del last para tratamiento de dato
        unique_together = ('first_name', 'last_name') #Nombre y apellido unico 
        
    def __str__(self):
        return str(self.id) + '-' + self.first_name + '-' + self.last_name + '-' + str(self.departamento)
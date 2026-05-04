from django.db import models

# Create your models here.
class Departamento(models.Model):
    name = models.CharField('Nombre', max_length=50, blank=True)
    #('Nombre', max_length=50, blank=True, null=True)
    #null no siempre va a registrar un campo 
    #blank se usa para decir que no es necesario colocar cierto campo 
    #por ejemplo name puede ser vacio
    #pero si se puede agregar el shor name y anulate 
    #con unique=True decimos que no queremos que ese parámetro aparezca en otro lado
    #editable=False para no dejar editar en admin/ un registro 
    #(importante en caso de que se necesite el dato pero no sea necesario mostrarlo o editarlo)
    shor_name = models.CharField('Nombre Corto', max_length=20, unique=True )
    anulate = models.BooleanField('Anulado', default=False)
    
    #Usamos la clase Meta para definir como se van a mostrar los nombre de las variables en admin/ o consultas
    class Meta:
        verbose_name = 'Mi departamento' #Asignar un nombre a mi clase models con formato amigable
        verbose_name_plural = 'Areas de la empresa' #Asignar al plurarl un nombre (hay casos donde se pluraliza una variable)
        ordering = ['-name'] #El orden en que se verán las consultas (sin el "-" se ordena ascendente A-Z sino lo contrario)
        unique_together = ('name', 'shor_name') #Restricción que indica que no se debe registrar los mismos campos dos veces.
        #Dos filas donde el name sea "Recursos Humanos" y el shor_name sea "RRHH" indica que no se puede hacer así
    
    def __str__(self):
        return str(self.id) + '-' + self.name + '-' + self.shor_name #Representa como se ven los datos en admin
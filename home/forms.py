from django import forms
from .models import Prueba

class PruebaForm(forms.ModelForm):
# Formularios model form o formularios simples
    class Meta:
        model = Prueba
        fields = (
            'titulo',
            'subtitulo',
            'cantidad',        
        )
        widgets = {
            'titulo': forms.TextInput(
                attrs = {
                    'placeholder': 'Ingrese el titulo'
                }
            )
        }

    def clean_cantidad(self):
        cantidad = self.cleaned_data['cantidad']
        if cantidad < 10: # Si el numero no es mayor a 10 no va a dejar guardar en la base de datos.
            raise forms.ValidationError('Ingresa un numero mayor a 10') #Formularios para validaciones
        return cantidad
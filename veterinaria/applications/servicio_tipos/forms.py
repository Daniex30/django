from django import forms

from .models import Servicio_tipo

class ServicioForm(forms.ModelForm):

    class Meta:
        model = Servicio_tipo
        fields = (
            'name',
        )
        widgets = {
            'name': forms.TextInput(
                attrs ={
                    'placeholder': 'Ingrese servicio aquí'
                }
            )
        }

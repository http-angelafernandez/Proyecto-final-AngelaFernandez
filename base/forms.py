from django import forms
from base.models import Personaje

class PersonajeForm(forms.ModelForm):
    class Meta:
        model = Personaje
        fields = ['libro', 'perfil', 'nombre', 'alias', 'genero', 'edad', 'nacimiento', 'ocupacion', 'estado', 'parientes', 'romances', 'descripcion']
        widgets = {
            'nacimiento': forms.DateInput(attrs={
                'type': 'date',
                'class': 'datepicker',
            }),
        }


from django import forms 
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User
from usuarios.models import DatosExtra

class CreacionDeUsuario(UserCreationForm):
    email = forms.EmailField()
    password1 = forms.CharField(label='password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repetir password', widget=forms.PasswordInput)
    first_name = forms.CharField (label='Nombre')
    last_name = forms.CharField (label='Apellido')

    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name', 'password1', 'password2']
        help_texts = {key: '' for key in fields}

class EdicionDePerfil(UserChangeForm):
    email = forms.EmailField (label='Correo electronico')
    first_name = forms.CharField (label='Nombre')
    last_name = forms.CharField (label='Apellido')
    password = None
    avatar = forms.ImageField(required=False)

    class Meta:
        model = User
        fields = ['email', 'first_name', 'last_name', 'avatar']

class DescripcionForm(forms.ModelForm):
    class Meta:
        model = DatosExtra
        fields = ['descripcion']
        widgets = {
            'descripcion': forms.TextInput(attrs={'placeholder': 'Escribe una breve descripción'}),
        }

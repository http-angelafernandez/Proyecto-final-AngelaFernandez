from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, UserChangeForm
from django.contrib.auth import authenticate, login as django_login
from usuarios.forms import CreacionDeUsuario, EdicionDePerfil, DescripcionForm
from django.views.generic.detail import DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import PasswordChangeView
from django.urls import reverse_lazy
from usuarios.models import DatosExtra, User



def login(request):
    
    formulario = AuthenticationForm
    
    if request.method == 'POST':
        formulario = AuthenticationForm(request, data=request.POST)
        if formulario.is_valid():
            usuario = formulario.get_user()

            django_login(request, usuario)

            DatosExtra.objects.get_or_create(user=usuario)

            return redirect('inicio') 

    return render(request, 'usuarios/login.html', {'form': formulario })

def register(request):
   
    formulario = CreacionDeUsuario()
    if request.method == 'POST':
        formulario = CreacionDeUsuario(request.POST)
        if formulario.is_valid():

            formulario.save()
 
            return redirect('usuarios:login')

   
    return render(request, 'usuarios/register.html', {'form': formulario })

def editar_perfil(request):
    datos_extra = request.user.datosextra
    formulario_perfil = EdicionDePerfil(instance=request.user, initial={'avatar': datos_extra.avatar})
    formulario_descripcion = DescripcionForm(instance=datos_extra)  

    if request.method == "POST":
        formulario_perfil = EdicionDePerfil(request.POST, request.FILES, instance=request.user)
        formulario_descripcion = DescripcionForm(request.POST, instance=datos_extra)

        if formulario_perfil.is_valid() and formulario_descripcion.is_valid():
            avatar_data = formulario_perfil.cleaned_data.get('avatar')
            
            if avatar_data:  
                datos_extra.avatar = avatar_data

            formulario_descripcion.save()  
            datos_extra.save() 
            formulario_perfil.save()  

            return redirect('inicio')

    return render(request, 'usuarios/editar_perfil.html', {
        'form': formulario_perfil,
        'form_descripcion': formulario_descripcion  
    })


    
class CambiarPassword(LoginRequiredMixin, PasswordChangeView):
    template_name = 'usuarios/cambiar_password.html'
    success_url = reverse_lazy('usuarios:editar_perfil')

class VerPerfil(LoginRequiredMixin, DetailView):
    model = User
    template_name = "usuarios/ver_perfil.html"
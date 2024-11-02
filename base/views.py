from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from base.models import Libro, Personaje
from base.forms import PersonajeForm
from django.urls import reverse_lazy
from django.views.generic.detail import DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django import forms


def inicio(request):
    return render(request, 'base.html')

def aboutme(request):
    return render(request, 'aboutme.html')

class CrearLibro(LoginRequiredMixin, CreateView):
    model = Libro
    template_name = "crear_libro.html"
    fields = ['portada', 'titulo', 'autor', 'sinopsis']

    def get_success_url(self):
        return reverse_lazy('ver_libro', kwargs={'pk': self.object.pk})

   
def ver_libro(request, pk):
    libro = Libro.objects.get(pk=pk)
    return render(request, 'ver_libro.html', {'libro': libro})

@login_required
def ver_sinopsis(request, pk):
    libro = Libro.objects.get(pk=pk)
    return render(request, 'ver_sinopsis.html', {'libro': libro})

class ListadoLibros(ListView):
    model = Libro
    template_name = "listado_libros.html"
    context_object_name = 'libros'

class EditarLibro(LoginRequiredMixin, UpdateView):
    model = Libro
    template_name = "editar_libro.html"
    success_url = reverse_lazy('listado_libros')
    fields = ['portada', 'titulo', 'autor', 'sinopsis']

class EliminarLibro(LoginRequiredMixin, DeleteView):
    model = Libro
    template_name = "eliminar_libro.html"
    success_url = reverse_lazy('listado_libros')

class CrearPersonaje(LoginRequiredMixin, CreateView):
    model = Personaje
    form_class = PersonajeForm  
    template_name = "crear_personaje.html"


    def get_success_url(self):
        return reverse_lazy('ver_personaje', kwargs={'pk': self.object.pk})

class VerPersonaje(DetailView):
    model = Personaje
    template_name = "ver_personaje.html"

class ListadoPersonajes(ListView):
    model = Personaje
    template_name = "listado_personajes.html"
    context_object_name = 'personajes'

class EditarPersonaje(LoginRequiredMixin, UpdateView):
    model = Personaje
    template_name = "editar_personaje.html"
    success_url = reverse_lazy('listado_personajes')
    fields = ['libro', 'perfil', 'nombre', 'alias', 'genero', 'edad', 'ocupacion', 'estado', 'parientes', 'romances', 'descripcion']

class EliminarPersonaje(LoginRequiredMixin, DeleteView):
    model = Personaje
    template_name = "eliminar_personaje.html"
    success_url = reverse_lazy('listado_personajes')

class VerMas(DetailView):
    model = Personaje
    template_name = "ver_mas.html"
    context_object_name = 'personaje'
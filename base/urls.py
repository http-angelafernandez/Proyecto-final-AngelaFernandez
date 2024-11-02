from django.urls import path
from base import views  
from base.views import ver_libro, ver_sinopsis

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('aboutme/', views.aboutme, name='about_me'),
    
    # Rutas para libros
    path('libros/crear/', views.CrearLibro.as_view(), name='crear_libro'),
    path('libros/', views.ListadoLibros.as_view(), name='listado_libros'),  
    path('ver-libro/<int:pk>/', ver_libro, name='ver_libro'),
    path('ver-sinopsis/<int:pk>/', ver_sinopsis, name='ver_sinopsis'),
    path('libros/<int:pk>/editar/', views.EditarLibro.as_view(), name='editar_libro'),
    path('libros/<int:pk>/eliminar/', views.EliminarLibro.as_view(), name='eliminar_libro'),
  
    # Rutas para personajes
    path('personajes/crear', views.CrearPersonaje.as_view(), name='crear_personaje'),
    path('personajes/', views.ListadoPersonajes.as_view(), name='listado_personajes'),  
    path('personajes/<int:pk>/', views.VerPersonaje.as_view(), name='ver_personaje'),
    path('personajes/<int:pk>/editar/', views.EditarPersonaje.as_view(), name='editar_personaje'),
    path('personajes/<int:pk>/eliminar/', views.EliminarPersonaje.as_view(), name='eliminar_personaje'),
    path('personajes/<int:pk>/info/', views.VerMas.as_view(), name='ver_mas')
]

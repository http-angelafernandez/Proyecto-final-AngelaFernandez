from django.db import models

# Create your models here.

class Libro(models.Model):
    portada = models.ImageField(upload_to='portadas', blank=True, null=False)
    titulo = models.CharField(max_length=50)
    autor = models.CharField(max_length=20)
    sinopsis = models.TextField(max_length=700)
    

    def __str__(self):
        return f'{self.titulo}'
    
class Personaje(models.Model):
    libro = models.CharField(max_length=50)
    perfil = models.ImageField(upload_to='personajes', blank=True, null=False)
    nombre = models.CharField(max_length=50)
    alias = models.TextField(max_length=600)
    genero = models.CharField(max_length=20)
    edad = models.IntegerField()
    ocupacion = models.CharField(max_length=50)
    estado = models.CharField(max_length=50)
    parientes = models.TextField(max_length=600)
    romances = models.TextField(max_length=600)
    descripcion = models.TextField(max_length=600)
    nacimiento = models.DateField(null=True, blank=True) 

    def __str__(self):
        return f'{self.nombre}'

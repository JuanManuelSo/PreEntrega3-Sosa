from django.db import models

# Create your models here.

class jugador(models.Model):
    nombre = models.CharField(max_length=60)
    edad = models.IntegerField()
    posicion = models.CharField(max_length=30)
    equipo = models.CharField(max_length=60)
    altura = models.FloatField()
    lesionado = models.BooleanField()
    activo = models.BooleanField()
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nombre


class entrenador(models.Model):
    nombre = models.CharField(max_length=60)
    equipo = models.CharField(max_length=60)
    edad = models.IntegerField()
    activo = models.BooleanField()
    created = models.DateTimeField(auto_now_add=True,)
    modified = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.nombre
    
class equipo(models.Model):
    nombre = models.CharField(max_length=60)
    añoFundado = models.DateField()
    campeonatos = models.IntegerField()
    localidad = models.CharField(max_length=60)
    created = models.DateTimeField(auto_now_add=True,)
    modified = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.nombre
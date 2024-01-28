from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class jugador(models.Model):
    nombre = models.CharField(max_length=60)
    edad = models.IntegerField()
    posicion = models.CharField(max_length=30)
    equipo = models.CharField(max_length=60)
    altura = models.FloatField()
    lesionado = models.BooleanField()
    activo = models.BooleanField()
    biografia = models.TextField(max_length = 7000,default='ValorPredeterminado')
    # Campo imagen, con un default en caso de no subir nati
    imagen = models.ImageField(upload_to='jugadores', default='jugadores/basketimagen.jpg')

    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Nombre:{self.nombre}"


class entrenador(models.Model):
    nombre = models.CharField(max_length=60)
    equipo = models.CharField(max_length=60)
    edad = models.IntegerField()
    activo = models.BooleanField()
    imagen = models.ImageField(upload_to='dt', default='dt/MOU.PNG')

    created = models.DateTimeField(auto_now_add=True,)
    modified = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"Nombre:{self.nombre}"
    
class equipo(models.Model):
    nombre = models.CharField(max_length=60)
    añoFundado = models.DateField()
    campeonatos = models.IntegerField()
    localidad = models.CharField(max_length=60)
    imagen = models.ImageField(upload_to='team', default='team/shield.jpg')

    created = models.DateTimeField(auto_now_add=True,)
    modified = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"Nombre:{self.nombre}"
    
class Avatar(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to="avatares",null=True,blank=True)

    class Meta:
        verbose_name = "Avatar"
        verbose_name_plural = "Avatares"
    
    def first(self,request):
        return self.filter(user=request.user.id)
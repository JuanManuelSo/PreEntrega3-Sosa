"""
URL configuration for entrega3 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from WebBasket.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    
    #path("WebBasket/",include("WebBasket.urls"))

    path("menu/",inicio, name = "Inicio"),
    
    #URL models creados
    path("agregar_jugadores/",players, name = "Jugadores"),
    path("agregar_entrenadores/",coach, name = "Entrenadores"),
    path("agregar_equipo/",team, name = "Equipos"),

    #URLs para crear nuevos datos
    path("nuevoJugador/",add_player, name = "Nuevojugador"),
    path("nuevoEntrenador/",add_coach, name = "Nuevoentrenador"),
    path("nuevoEquipo/",add_team, name = "Nuevoequipo"),
    
    
    path("buscarJugador/",search_player, name = "Buscarjugador"),
    path("resultadoEquipo/",resultado, name = "Resultadojugador"),

]

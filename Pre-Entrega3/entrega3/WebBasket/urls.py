from django.urls import path
from WebBasket.views import *

urlpatterns = [
    path("menu/",inicio, name = "Inicio"),
    
    #URL models creados
    path("agregar_jugadores/",players, name = "Jugadores"),
    path("agregar_entrenadores/",coach, name = "Entrenadores"),
    path("agregar_equipo/",team, name = "Equipos"),

    #URLs para crear nuevos datos
    path("nuevoJugador/",add_player),
    path("nuevoEntrenador/",add_coach),
    path("nuevoEquipo/",add_team),
    
    
    path("buscarJugador/",search_player),
    path("resultadoEquipo/",resultado),


]
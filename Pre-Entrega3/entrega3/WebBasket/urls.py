from django.urls import path
from WebBasket.views import *
from django.contrib.auth.views import LogoutView

urlpatterns = [
    #PRINCIPALES
    path("menu/",inicio, name = "Inicio"),
    path("login/",inicioSesion, name = "Login"),
    path("registro/",register, name = "SignUp"),
    path("logout/",cerrar_sesion, name = "Logout"),
    path("editar/",editarUsuarios, name = "Editar"),
    path("agregar/",agregarAvatar, name = "Avatar"),
    path("sobremi/",agregarAvatar, name = "Sobremi"),

    
    #URL models creados
    path("agregar_jugadores/",players, name = "Jugadores"),
    path("agregar_entrenadores/",coach, name = "Entrenadores"),
    path("agregar_equipo/",team, name = "Equipos"),

   
    path("buscarJugador/",search_player, name = "Buscarjugador"),
    path("resultadoEquipo/",resultado, name = "Resultadojugador"),


    #URLs leer,eliminar,editar (JUGADORES)
    path("leerJugadores/",leerJugadores, name = "LeerJugador"),
    path("eliminarJugadores/<jugNom>/",eliminarJugadores, name = "EliminarJugador"),
    path("editarJugadores/<jugNom>/",editarJugadores, name = "EditarJugador"),


    #URLs leer,eliminar,editar (ENTRENADORES)
    path("leerEntrenadores/",leerEntrenadores, name = "LeerEntrenador"),
    path("eliminarEntrenadores/<entNom>/",eliminarEntrenadores, name = "EliminarEntrenador"),
    path("editarEntrenadores/<entNom>/",editarEntrenadores, name = "EditarEntrenador"),


    #URLs leer,eliminar,editar (EQUIPOS)
    path("leerEquipos/",leerEquipos, name = "LeerEquipo"),
    path("eliminarEquipos/<eqpNom>/",eliminarEquipos, name = "EliminarEquipo"),
    path("editarEquipos/<eqpNom>/",editarEquipos, name = "EditarEquipo"),
]

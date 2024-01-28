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
from django.contrib.auth.views import LogoutView
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    
    #path("WebBasket/",include("WebBasket.urls"))

    #PRINCIPALES
    path("menu/",inicio, name = "Inicio"),
    path("login/",inicioSesion, name = "Login"),
    path("registro/",register, name = "SignUp"),
    path("logout/",cerrar_sesion, name = "Logout"),
    path("editar/",editarUsuarios, name = "Editar"),
    path("agregar/",agregarAvatar, name = "Avatar"),
    path("sobremi/",sobreMi, name = "Sobremi"),

    
    #URL models creados
    path("agregar_jugadores/",players, name = "Jugadores"),
    path("agregar_entrenadores/",coach, name = "Entrenadores"),
    path("agregar_equipo/",team, name = "Equipos"),


    #URL Busqueda
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
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
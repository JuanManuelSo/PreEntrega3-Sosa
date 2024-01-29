# PROYECTO FINAL-SOSA

# Mi pagina web tiene los siguientes modelos:
1- Menu(Buscar jugador por equipo)
2- Jugador
3- Entrenador
4- Equipo

# Mi URLS son: 
path('admin/', admin.site.urls),
    

#PRINCIPALES
menu/",inicio, name = "Inicio"),
login/",inicioSesion, name = "Login"),
registro/",register, name = "SignUp"),
logout/",cerrar_sesion, name = "Logout"),
editar/",editarUsuarios, name = "Editar"),
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

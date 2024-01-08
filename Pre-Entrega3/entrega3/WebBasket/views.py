from django.shortcuts import render
from .models import *
from .forms import *
from django.http import HttpResponse

# Create your views here.

def inicio(request):
    return render(request,"WebBasket/inicio.html")

def players(request):
    return render(request,"WebBasket/jugadores.html")

def coach(request):
    return render(request,"WebBasket/entrenadores.html")

def team(request):
    return render(request,"WebBasket/equipos.html")

def add_player(request):

    if request.method == "POST":
        nuevo_formulario = JugadorFormulario(request.POST)

        if nuevo_formulario .is_valid():
            info = nuevo_formulario.cleaned_data
            nuevo_jugador = jugador(nombre=info["nombre"],edad =info["edad"],posicion=info["posicion"],equipo=info["equipo"],altura=info["altura"],
                                    lesionado=info["lesionado"],activo=info["activo"])
            nuevo_jugador.save()
            
            return render(request,"WebBasket/inicio.html")
    else:
        nuevo_formulario = JugadorFormulario()

    return render(request,"WebBasket/addPlayer.html",{"miJugador":nuevo_formulario})

def add_coach(request):

    if request.method == "POST":
        nuevo_formulario = EntrenadorFormulario(request.POST)

        if nuevo_formulario .is_valid():
            info = nuevo_formulario.cleaned_data
            nuevo_entrenador = entrenador(nombre=info["nombre"],equipo=info["equipo"],edad =info["edad"],activo=info["activo"])
            nuevo_entrenador.save()
            
            return render(request,"WebBasket/inicio.html")
    else:
        nuevo_formulario = EntrenadorFormulario()

    return render(request,"WebBasket/addCoach.html",{"miEntrenador":nuevo_formulario})

def add_team(request):

    if request.method == "POST":
        nuevo_formulario = EquipoFormulario(request.POST)

        if nuevo_formulario .is_valid():
            info = nuevo_formulario.cleaned_data
            nuevo_equipo = equipo(nombre=info["nombre"],añoFundado=info["añoFundado"],campeonatos =info["campeonatos"],localidad=info["localidad"])
            nuevo_equipo.save()
            
            return render(request,"WebBasket/inicio.html")
    else:
        nuevo_formulario = EquipoFormulario()

    return render(request,"WebBasket/addTeam.html",{"miEquipo":nuevo_formulario})

def search_player(request):

    return render(request,"WebBasket/buscarjugador.html")

def resultado(request):

    if request.method == "GET":
        team_pedido = request.GET["team"]
        resultado_jugadores = jugador.objects.filter(equipo__icontains = team_pedido)

    return render(request,"WebBasket/buscarjugador.html", {"jugadores":resultado_jugadores})
from django.shortcuts import render
from .models import *
from .forms import *
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required


# Create your views here.

def inicioSesion(request):
    
    if request.method == "POST":
        form = AuthenticationForm(request, data = request.POST)
        if form.is_valid():

            usuario = form.cleaned_data.get("username")
            contraseña = form.cleaned_data.get("password")

            user = authenticate(username = usuario, password = contraseña)

            if user:
                login(request,user)

                return render(request, "WebBasket/principales/inicio.html", {"mensaje":f"¡Bienvenido a WIKIBASKET! {user}"})
        else:
             return render(request, "WebBasket/principales/inicio.html",{"mensaje":"Datos Incorrectos!"})
    else:
        form = AuthenticationForm(request)

    return render(request, "WebBasket/registro/login.html",{"formularioSesion":form})
    
def register(request):

    if request.method == "POST":
        form = UsuarioRegistro(request.POST)

        if form.is_valid():

            username = form.cleaned_data["username"]
            form.save()
            return render(request,"WebBasket/principales/inicio.html",{"mensaje":"Usuario creado con exito!"})
    else:
        form = UsuarioRegistro()

    return render(request,"WebBasket/registro/registro.html",{"formularioRegistro":form})  

@login_required
def cerrar_sesion(request):
    logout(request)

    return render(request,"WebBasket/registro/cerrarSesion.html")


@login_required
def editarUsuarios(request):
    usuario = request.user
    if request.method == "POST":

        form = FormularioEditar(request.POST)
        if form.is_valid():
            info = form.cleaned_data

            usuario.email = info["email"]
            usuario.set_password(info["password1"])
            usuario.first_name = info["first_name"]
            usuario.last_name = info["last_name"]
            usuario.save()

            return render(request,"WebBasket/principales/inicio.html",{"mensaje":"Usuario editado con exito!"})
    else:
        form = FormularioEditar(initial={
            "email":usuario.email,
            "first_name":usuario.first_name,
            "last_name":usuario.last_name,
            })
    return render(request,"WebBasket/editarPerfil.html",{"formulario":form,"usuario":usuario})

def inicio(request):

    mensaje = "Bienvendios a WIKIBASKET!!"
    contexto = {"mensaje":mensaje}
    return render(request,"WebBasket/principales/inicio.html",{"mensaje":mensaje})

@login_required
def players(request):
    if request.method == "POST":
        nuevo_formulario = JugadorFormulario(request.POST, request.FILES)
        if nuevo_formulario .is_valid():
            info = nuevo_formulario.cleaned_data
            nuevo_jugador = jugador(nombre=info["nombre"],edad =info["edad"],posicion=info["posicion"],equipo=info["equipo"],altura=info["altura"],
                                    lesionado=info["lesionado"],activo=info["activo"],biografia=info["biografia"], imagen=request.FILES.get('imagen', "jugadores/basketimagen.jpg") )
            
            nuevo_jugador.save()
            
            return render(request,"WebBasket/principales/inicio.html",{"mensaje":"Jugador agregado con exito!"})
    else:
        nuevo_formulario = JugadorFormulario()

    return render(request,"WebBasket/addPlayer.html",{"miJugador":nuevo_formulario})

@login_required
def coach(request):
    if request.method == "POST":
        nuevo_formulario = EntrenadorFormulario(request.POST,request.FILES)

        if nuevo_formulario .is_valid():
            info = nuevo_formulario.cleaned_data
            nuevo_entrenador = entrenador(nombre=info["nombre"],equipo=info["equipo"],edad =info["edad"],activo=info["activo"], imagen=request.FILES.get('imagen', "jugadores/basketimagen.jpg") )
            
            nuevo_entrenador.save()
            
            return render(request,"WebBasket/principales/inicio.html",{"mensaje":"Entrenador agregado con exito!"})
    else:
        nuevo_formulario = EntrenadorFormulario()

    return render(request,"WebBasket/addCoach.html",{"miEntrenador":nuevo_formulario})

@login_required
def team(request):
    if request.method == "POST":
        nuevo_formulario = EquipoFormulario(request.POST,request.FILES)

        if nuevo_formulario .is_valid():
            info = nuevo_formulario.cleaned_data
            nuevo_equipo = equipo(nombre=info["nombre"],añoFundado=info["añoFundado"],campeonatos =info["campeonatos"],localidad=info["localidad"], imagen=request.FILES.get('imagen', "jugadores/basketimagen.jpg") )
            
            nuevo_equipo.save()
            
            return render(request,"WebBasket/principales/inicio.html",{"mensaje":"Equipo agregado con exito!"})
    else:
        nuevo_formulario = EquipoFormulario()

    return render(request,"WebBasket/addTeam.html",{"miEquipo":nuevo_formulario})

def search_player(request):

    return render(request,"WebBasket/busqueda/buscarjugador.html")

def resultado(request):

    if request.method == "GET":
        team_pedido = request.GET["team"]

        resultado_entrenador = entrenador.objects.filter(equipo__icontains = team_pedido)
        resultado_jugadores = jugador.objects.filter(equipo__icontains = team_pedido)

    return render(request,"WebBasket/busqueda/buscarjugador.html", {"jugadores":resultado_jugadores,"entrenadores":resultado_entrenador})

@login_required
def leerJugadores(request):
    jugadores = jugador.objects.all()
    contexto = {"players":jugadores}
    return render(request,"WebBasket/leerjugadores.html",contexto)

def eliminarJugadores(request, jugNom):
    Jugador = jugador.objects.get(nombre=jugNom)
    Jugador.delete()

    jugadores = jugador.objects.all()
    contexto = {"players":jugadores}
    return render(request,"WebBasket/leerjugadores.html",contexto)

def editarJugadores(request,jugNom):
    Jugador = jugador.objects.get(nombre=jugNom)

    if request.method == "POST":
        nuevo_formulario = JugadorFormulario(request.POST)

        if nuevo_formulario .is_valid():
            info = nuevo_formulario.cleaned_data
            
            Jugador.nombre = info["nombre"]
            Jugador.edad = info["edad"]
            Jugador.posicion = info["posicion"]
            Jugador.equipo = info["equipo"]
            Jugador.altura = info["altura"]
            Jugador.lesionado = info["lesionado"]
            Jugador.activo = info["activo"]
            Jugador.biografia = info["biografia"]


            Jugador.save()
            return render(request,"WebBasket/principales/inicio.html",{"mensaje":"Edicion Exitosa!"})
    else:
        print(Jugador)
        nuevo_formulario = JugadorFormulario(initial={"nombre":Jugador.nombre,"edad":Jugador.edad,"posicion":Jugador.posicion,"equipo":Jugador.equipo,
                                                      "altura":Jugador.altura,"lesionado":Jugador.lesionado,"activo":Jugador.activo,"biografia":Jugador.biografia,})
        # nuevo_formulario = JugadorFormulario(initial=Jugador)

    return render(request,"WebBasket/editarPlayer.html",{"miJugador":nuevo_formulario, "nombre":jugNom})

@login_required
def leerEntrenadores(request):
    Entrenadores = entrenador.objects.all()
    contexto = {"coachs":Entrenadores}
    return render(request,"WebBasket/leerentrenadores.html",contexto)

def eliminarEntrenadores(request,entNom):
    Entrenador = entrenador.objects.get(nombre=entNom)
    Entrenador.delete()

    Entrenadores = entrenador.objects.all()
    contexto = {"coachs":Entrenadores}
    return render(request,"WebBasket/leerentrenadores.html",contexto)

def editarEntrenadores(request,entNom):
    Entrenador = entrenador.objects.get(nombre=entNom)

    if request.method == "POST":
        nuevo_formulario = EntrenadorFormulario(request.POST)

        if nuevo_formulario .is_valid():
            info = nuevo_formulario.cleaned_data

            Entrenador.nombre = info["nombre"]
            Entrenador.equipo = info["equipo"] 
            Entrenador.edad = info["edad"] 
            Entrenador.activo = info["activo"]
            

            
            Entrenador.save()
            
            return render(request,"WebBasket/principales/inicio.html",{"mensaje":"Edicion Exitosa!"})
    else:
        nuevo_formulario = EntrenadorFormulario(initial={"Nombre":Entrenador.nombre,"Equipo":Entrenador.equipo,"Edad":Entrenador.edad,
                                                         "Activo":Entrenador.activo})

    return render(request,"WebBasket/editarCoach.html",{"miEntrenador":nuevo_formulario,"nombre":entNom})

@login_required
def leerEquipos(request):
    Equipos = equipo.objects.all()
    contexto = {"team":Equipos}
    return render(request,"WebBasket/leerequipos.html",contexto)

def eliminarEquipos(request,eqpNom):
    Equipo = equipo.objects.get(nombre = eqpNom)
    Equipo.delete()

    Equipos = equipo.objects.all()
    contexto = {"team":Equipos}
    return render(request,"WebBasket/leerequipos.html",contexto)

def editarEquipos(request,eqpNom):
    Equipo = equipo.objects.get(nombre = eqpNom)

    if request.method == "POST":
        nuevo_formulario = EquipoFormulario(request.POST)

        if nuevo_formulario .is_valid():
            info = nuevo_formulario.cleaned_data
            
            Equipo.nombre = info["nombre"]
            Equipo.añoFundado = info["añoFundado"]
            Equipo.campeonatos = info["campeonatos"]
            Equipo.localidad = info["localidad"]
            
            
            Equipo.save()
            
            return render(request,"WebBasket/principales/inicio.html",{"mensaje":"Edicion Exitosa!"})
    else:
        nuevo_formulario = EquipoFormulario(initial={"Nombre":Equipo.nombre,"Año Fundado":Equipo.añoFundado,"Campeonatos":Equipo.campeonatos,
                                                     "Localidad":Equipo.localidad})

    return render(request,"WebBasket/editarTeam.html",{"miEquipo":nuevo_formulario, "nombre":eqpNom})


@login_required
def agregarAvatar(request):
    if request.method == "POST":

        form = AvatarFormulario(request.POST,request.FILES)

        if form.is_valid():

            usuarioActual = User.objects.get(username=request.user)

            avatar = Avatar(usuario=usuarioActual,imagen = form.cleaned_data["imagen"])

            avatar.save()

            return render(request, "WebBasket/principales/inicio.html",{"mensaje":"Avatar editado!"})
        
    else:
        form = AvatarFormulario()
    
    return render(request,"WebBasket/registro/agregarAvatar.html",{"formulario":form})

def sobreMi(request):
    mensaje = "SOBRE MI"

    return render(request, "WebBasket/sobreMi.html", {'mensaje': mensaje})

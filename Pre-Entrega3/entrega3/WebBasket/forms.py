from django import forms

class JugadorFormulario (forms.Form):
    nombre = forms.CharField(max_length=60)
    edad = forms.IntegerField()
    posicion = forms.CharField(max_length=30)
    equipo = forms.CharField(max_length=60)
    altura = forms.FloatField()
    lesionado = forms.BooleanField()
    activo = forms.BooleanField()

class EntrenadorFormulario (forms.Form):
    nombre = forms.CharField(max_length=60)
    equipo = forms.CharField(max_length=60)
    edad = forms.IntegerField()
    activo = forms.BooleanField()

class EquipoFormulario (forms.Form):
    nombre = forms.CharField(max_length=60)
    añoFundado = forms.DateField()
    campeonatos = forms.IntegerField()
    localidad = forms.CharField(max_length=60)
    
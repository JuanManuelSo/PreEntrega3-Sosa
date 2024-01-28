from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import User
from .models import *
from django.utils.safestring import SafeString


class JugadorFormulario (forms.Form):

    def __init__(self, *args, **kwargs):
        super(JugadorFormulario, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-god'

    def as_div(self):
        return SafeString(super().as_div().replace("<div>", "<div class='form-insta'>"))

    nombre = forms.CharField(max_length=60)
    edad = forms.IntegerField()
    posicion = forms.CharField(max_length=30)
    equipo = forms.CharField(max_length=60)
    altura = forms.FloatField()
    lesionado = forms.BooleanField(required=False)
    activo = forms.BooleanField(required=False)
    biografia = forms.CharField(widget=forms.Textarea)
    imagen = forms.ImageField(required=False)




class EntrenadorFormulario (forms.Form):
    def __init__(self, *args, **kwargs):
        super(EntrenadorFormulario, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-god'

    def as_div(self):
        return SafeString(super().as_div().replace("<div>", "<div class='form-insta'>"))

    nombre = forms.CharField(max_length=60)
    equipo = forms.CharField(max_length=60)
    edad = forms.IntegerField()
    activo = forms.BooleanField(required=False)
    imagen = forms.ImageField(required=False)

class EquipoFormulario (forms.Form):
    def __init__(self, *args, **kwargs):
        super(EquipoFormulario, self).__init__(*args, **kwargs)
        # Agrega la clase 
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-god'

    def as_div(self):
        return SafeString(super().as_div().replace("<div>", "<div class='form-insta'>"))

    nombre = forms.CharField(max_length=60)
    añoFundado = forms.DateField()
    campeonatos = forms.IntegerField()
    localidad = forms.CharField(max_length=60)
    imagen = forms.ImageField(required=False)

class UsuarioRegistro (UserCreationForm):

    email = forms.EmailField()
    password1 = forms.CharField(label= "Contraseña", widget=forms.PasswordInput)
    password2 = forms.CharField(label= "Repetir la Contraseña", widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ["username","email","first_name","last_name","password1","password2"]


class FormularioEditar(UserCreationForm):
    email = forms.EmailField()
    password1 = forms.CharField(label= "Contraseña", widget=forms.PasswordInput)
    password2 = forms.CharField(label= "Repetir la Contraseña", widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ["email","first_name","last_name","password1","password2"]

class AvatarFormulario(forms.ModelForm):
    class Meta:
        model = Avatar
        fields = ["imagen"]
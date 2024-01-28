from django.contrib import admin
from WebBasket.models import *

# Register your models here.

class PostAdmin(admin.ModelAdmin):
    readonly_fields =("created","modified")

admin.site.register(jugador)
admin.site.register(entrenador)
admin.site.register(equipo)
admin.site.register(Avatar)


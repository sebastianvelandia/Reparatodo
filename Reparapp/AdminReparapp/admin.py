from django.contrib import admin
from .models import Agente,TecnicoEspecialista,Operador, Usuario
from AgenteReparapp.models import Orden,Cliente,Producto
from TecnicoReparapp.models import Taller, CallCenter
# Register your models here.
# admin.site.register(Agente)
# admin.site.register(Operador)
# admin.site.register(TecnicoEspecialista)
# admin.site.register(Orden)
# admin.site.register(Cliente)
# admin.site.register(Usuario)
admin.site.register(Taller)
admin.site.register(CallCenter)
# admin.site.register(Producto)
from django.contrib import admin
from .models import Agente,TecnicoEspecialista,Operador
from AgenteReparapp.models import Orden,Cliente
# Register your models here.
admin.site.register(Agente)
admin.site.register(Operador)
admin.site.register(TecnicoEspecialista)
admin.site.register(Orden)
admin.site.register(Cliente)
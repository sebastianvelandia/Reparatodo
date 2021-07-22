from django.urls import path
from django.contrib.auth.decorators import login_required
from .views import *

urlpatterns = [

    path('agregar_agente/', login_required(AgregarAgente.as_view()), name='agregar_agente'),
    path('listar_agentes/', login_required(ListadoAgente.as_view()), name='listar_agentes'),
    path('actualizar_agente/<int:pk>', login_required(ActualizarAgente.as_view()), name='actualizar_agente'),
    path('eliminar_agente/<int:pk>', login_required(EliminarAgente.as_view()), name ='eliminar_agente'),

    path('agregar_operador/', login_required(AgregarOperador.as_view()), name='agregar_operador'),
    path('listar_operadores/', login_required(ListadoOperador.as_view()), name='listar_operadores'),
    path('actualizar_operador/<int:pk>', login_required(ActualizarOperador.as_view()), name='actualizar_operador'),
    path('eliminar_operador/<int:pk>', login_required(EliminarOperador.as_view()), name ='eliminar_operador'),

    path('agregar_tecnico/', login_required(AgregarTecnico.as_view()), name='agregar_tecnico'),
    path('listar_tecnicos/', login_required(ListadoTecnico.as_view()), name='listar_tecnicos'),
    path('actualizar_tecnico/<int:pk>', login_required(ActualizarTecnico.as_view()), name='actualizar_tecnico'),
    path('eliminar_tecnico/<int:pk>', login_required(EliminarTecnico.as_view()), name ='eliminar_tecnico'),
]
from django.urls import path
from .views import ListadoAgente, ActualizarAgente, AgregarAgente, EliminarAgente, AgregarTecnico

urlpatterns = [

    path('agregar_agente/', AgregarAgente.as_view(), name='agregar_agente'),
    path('listar_agentes/', ListadoAgente.as_view(), name='listar_agentes'),
    path('actualizar_agente/<int:pk>', ActualizarAgente.as_view(), name='actualizar_agente'),
    path('eliminar_agente/<int:pk>', EliminarAgente.as_view(), name ='eliminar_agente'),
    
    path('agregar_tecnico/', AgregarTecnico.as_view(), name='agregar_tecnico'),
    path('listar_tecnicos/', ListadoAgente.as_view(), name='listar_tecnicos'),
    path('actualizar_tecnico/<int:pk>', ActualizarAgente.as_view(), name='actualizar_tecnico'),
    path('eliminar_tecnico/<int:pk>', EliminarAgente.as_view(), name ='eliminar_tecnico'),
]

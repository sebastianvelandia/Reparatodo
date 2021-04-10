from django.urls import path
from .views import *
urlpatterns = [

    path('agregar_taller/', AgregarTaller.as_view(), name='agregar_taller'),
    path('listar_talleres/', ListadoTaller.as_view(), name='listar_talleres'),
    path('actualizar_taller/<int:pk>', ActualizarTaller.as_view(), name='actualizar_taller'),
    path('eliminar_taller/<int:pk>', EliminarTaller.as_view(), name ='eliminar_taller'),
    
    path('agregar_callcenter/', AgregarCallCenter.as_view(), name='agregar_callcenter'),
    path('listar_callcenters/', ListadoCallCenter.as_view(), name='listar_callcenters'),
    path('actualizar_callcenter/<int:pk>', ActualizarCallCenter.as_view(), name='actualizar_callcenter'),
    path('eliminar_callcenter/<int:pk>', EliminarCallCenter.as_view(), name ='eliminar_callcenter'),
]

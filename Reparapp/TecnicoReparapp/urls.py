from django.urls import path

from .views import *
urlpatterns = [
    path('mis_ordenes/<id>', consultarOrden, name= 'mis_ordenes'),
    path('detalle_orden/<int:pk>', OrdenDetailView.as_view(), name= 'detalle_orden'),
    path('actualizar_orden/<int:pk>', ActualizarOrden.as_view(), name= 'actualizar_orden'),
    path('reparar_orden/<int:pk>', RepararOrden.as_view(), name= 'reparar_orden'),
    path('listar_ordenes/', ListadoOrdenes.as_view(), name='listar_ordenes'),

    path('listar_facturas/', ListarFacturas.as_view(), name='listar_facturas'),
    path('actualizar_factura/<int:pk>', EnviarOrden.as_view(), name='actualizar_factura'),

    # path('agregar_taller/', AgregarTaller.as_view(), name='agregar_taller'),
    # path('listar_talleres/', ListadoTaller.as_view(), name='listar_talleres'),
    # path('actualizar_taller/<int:pk>', ActualizarTaller.as_view(), name='actualizar_taller'),
    # path('eliminar_taller/<int:pk>', EliminarTaller.as_view(), name ='eliminar_taller'),
    
    # path('agregar_callcenter/', AgregarCallCenter.as_view(), name='agregar_callcenter'),
    # path('listar_callcenters/', ListadoCallCenter.as_view(), name='listar_callcenters'),
    # path('actualizar_callcenter/<int:pk>', ActualizarCallCenter.as_view(), name='actualizar_callcenter'),
    # path('eliminar_callcenter/<int:pk>', EliminarCallCenter.as_view(), name ='eliminar_callcenter'),

]

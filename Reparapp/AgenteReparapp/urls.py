from django.urls import path
from .views import *
urlpatterns = [

    path('agregar_cliente/', AgregarCliente.as_view(), name='agregar_cliente'),
    path('listar_clientes/', ListadoCliente.as_view(), name='listar_clientes'),
    path('actualizar_cliente/<int:pk>', ActualizarCliente.as_view(), name='actualizar_cliente'),
    path('eliminar_cliente/<int:pk>', EliminarCliente.as_view(), name ='eliminar_cliente'),
    
    path('agregar_producto/', AgregarProducto.as_view(), name='agregar_producto'),
    path('listar_productos/', ListadoProducto.as_view(), name='listar_productos'),
    path('actualizar_producto/<int:pk>', ActualizarProducto.as_view(), name='actualizar_producto'),
    path('eliminar_producto/<int:pk>', EliminarProducto.as_view(), name ='eliminar_producto'),

    path('agregar_orden/', AgregarOrden.as_view(), name='agregar_orden'),
    path('listar_ordenes/', ListadoOrden.as_view(), name='listar_ordenes'),
    path('actualizar_orden/<int:pk>', ActualizarOrden.as_view(), name='actualizar_orden'),
    path('eliminar_orden/<int:pk>', EliminarOrden.as_view(), name ='eliminar_orden'),

    path('agregar_factura/', AgregarFactura.as_view(), name='agregar_factura'),
    path('listar_facturas/', ListadoFactura.as_view(), name='listar_facturas'),
    path('actualizar_factura/<int:pk>', ActualizarFactura.as_view(), name='actualizar_factura'),
    path('eliminar_factura/<int:pk>', EliminarFactura.as_view(), name ='eliminar_factura'),
]

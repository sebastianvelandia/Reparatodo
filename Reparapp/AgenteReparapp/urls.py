from django.urls import path
from django.contrib.auth.decorators import login_required
from .views import *
urlpatterns = [

    path('agregar_cliente/', login_required(AgregarCliente.as_view()), name='agregar_cliente'),
    path('listar_clientes/', login_required(ListadoCliente.as_view()), name='listar_clientes'),
    path('actualizar_cliente/<int:pk>', login_required(ActualizarCliente.as_view()), name='actualizar_cliente'),
    path('eliminar_cliente/<int:pk>', login_required(EliminarCliente.as_view()), name ='eliminar_cliente'),
    
    path('agregar_producto/', login_required(AgregarProducto.as_view()), name='agregar_producto'),
    path('listar_productos/', login_required(ListadoProducto.as_view()), name='listar_productos'),
    path('actualizar_producto/<int:pk>', login_required(ActualizarProducto.as_view()), name='actualizar_producto'),
    path('eliminar_producto/<int:pk>', login_required(EliminarProducto.as_view()), name ='eliminar_producto'),

    path('agregar_orden/', login_required(AgregarOrden.as_view()), name='agregar_orden'),
    path('listar_ordenes/', login_required(ListadoOrden.as_view()), name='listar_ordenes'),
    path('actualizar_orden/<int:pk>', login_required(ActualizarOrden.as_view()), name='actualizar_orden'),
    path('eliminar_orden/<int:pk>', login_required(EliminarOrden.as_view()), name ='eliminar_orden'),

    path('agregar_factura/', login_required(AgregarFactura.as_view()), name='agregar_factura'),
    path('listar_facturas/', login_required(ListadoFactura.as_view()), name='listar_facturas'),
    path('actualizar_factura/<int:pk>', login_required(ActualizarFactura.as_view()), name='actualizar_factura'),
    path('eliminar_factura/<int:pk>', login_required(EliminarFactura.as_view()), name ='eliminar_factura'),
]

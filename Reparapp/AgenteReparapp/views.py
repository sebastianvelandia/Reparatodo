from django.shortcuts import render, redirect
from django.views.generic.edit import FormView
from django.views.generic import TemplateView, ListView, UpdateView, CreateView, DeleteView
from django.urls import reverse_lazy
from .forms import ClienteForm, ProductoForm, OrdenForm, FacturaForm, NuevaOrdenForm
from .models import Cliente, Producto, Orden, Factura
from django.shortcuts import render

class ListadoCliente(ListView):
    model = Cliente
    template_name = 'AgenteReparapp/listar_clientes.html'
    context_object_name = 'clientes'
    queryset = Cliente.objects.all()

class ActualizarCliente(UpdateView):
    model = Cliente
    form_class = ClienteForm
    template_name = 'AgenteReparapp/editar_cliente.html'
    success_url = reverse_lazy('agente:listar_clientes')

class AgregarCliente(CreateView):
    model = Cliente
    form_class = ClienteForm
    template_name = 'AgenteReparapp/agregar_cliente.html'
    success_url = reverse_lazy('agente:listar_clientes')

class EliminarCliente(DeleteView):
    model = Cliente
    success_url = reverse_lazy('agente:listar_clientes')

class ListadoProducto(ListView):
    model = Producto
    template_name = 'AgenteReparapp/listar_productos.html'
    context_object_name = 'productos'
    queryset = Producto.objects.all()

class ActualizarProducto(UpdateView):
    model = Producto
    form_class = ProductoForm
    template_name = 'AgenteReparapp/editar_producto.html'
    success_url = reverse_lazy('agente:listar_productos')

class AgregarProducto(CreateView):
    model = Producto
    form_class = ProductoForm
    template_name = 'AgenteReparapp/agregar_producto.html'
    success_url = reverse_lazy('agente:listar_productos')

class EliminarProducto(DeleteView):
    model = Producto
    success_url = reverse_lazy('agente:listar_productos')

class ListadoOrden(ListView):
    model = Orden
    template_name = 'AgenteReparapp/listar_ordenes.html'
    context_object_name = 'ordenes'
    queryset = Orden.objects.all()

class ActualizarOrden(UpdateView):
    model = Orden
    form_class = OrdenForm
    template_name = 'AgenteReparapp/editar_orden.html'
    success_url = reverse_lazy('agente:listar_ordenes')

class AgregarOrden(CreateView):
    model = Orden
    form_class = NuevaOrdenForm
    template_name = 'AgenteReparapp/agregar_orden.html'
    success_url = reverse_lazy('agente:listar_ordenes')

class EliminarOrden(DeleteView):
    model = Orden
    success_url = reverse_lazy('agente:listar_ordenes')

class ListadoFactura(ListView):
    model = Factura
    template_name = 'AgenteReparapp/listar_facturas.html'
    context_object_name = 'facturas'
    queryset = Factura.objects.all()

class ActualizarFactura(UpdateView):
    model = Factura
    form_class = FacturaForm
    template_name = 'AgenteReparapp/editar_factura.html'
    success_url = reverse_lazy('agente:listar_facturas')

class AgregarFactura(CreateView):
    model = Factura
    form_class = FacturaForm
    template_name = 'AgenteReparapp/agregar_factura.html'
    success_url = reverse_lazy('agente:listar_facturas')

class EliminarFactura(DeleteView):
    model = Factura
    success_url = reverse_lazy('agente:listar_facturas')

class Consulta(TemplateView):
    template_name='inicio/consulta.html'

def consultarOrden(request):
    queryset=request.GET.get('buscar')
    orden=Orden.objects.all()
    print(queryset)
    if queryset: 
        orden=Orden.objects.filter(orden_id=queryset)
    return render(request,'inicio/consulta.html',{'orden': orden})
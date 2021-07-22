from AdminReparapp.models import Agente, Usuario
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages
from django.shortcuts import render, redirect
from django.views.generic.edit import FormView
from django.views.generic import TemplateView, ListView, UpdateView, CreateView, DeleteView
from django.urls import reverse_lazy
from .forms import ClienteForm, InformarOrdenForm, NuevaFacturaForm, NuevaOrdenForm, ProductoForm, OrdenForm, FacturaForm, NuevaOrdenClienteForm
from .models import Cliente, Producto, Orden, Factura
from django.shortcuts import render


class ListadoCliente(ListView):
    model = Cliente
    template_name = 'AgenteReparapp/listar_clientes.html'
    context_object_name = 'clientes'
    queryset = Cliente.objects.all()


class AgregarCliente(SuccessMessageMixin, CreateView):
    model = Cliente
    form_class = ClienteForm
    template_name = 'AgenteReparapp/agregar_cliente.html'
    success_url = reverse_lazy('agente:listar_clientes')
    success_message = "El Cliente fue creado correctamente"


class ActualizarCliente(SuccessMessageMixin, UpdateView):
    model = Cliente
    form_class = ClienteForm
    template_name = 'AgenteReparapp/editar_cliente.html'
    success_url = reverse_lazy('agente:listar_clientes')
    success_message = "El Cliente fue modificado correctamente"


class EliminarCliente(SuccessMessageMixin, DeleteView):
    model = Cliente
    success_url = reverse_lazy('agente:listar_clientes')
    success_message = "El Cliente fue eliminado correctamente"

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, self.success_message)
        return super(EliminarCliente, self).delete(request, *args, **kwargs)


class ListadoProducto(ListView):
    model = Producto
    template_name = 'AgenteReparapp/listar_productos.html'
    context_object_name = 'productos'
    queryset = Producto.objects.all()


class AgregarProducto(SuccessMessageMixin, CreateView):
    model = Producto
    form_class = ProductoForm
    template_name = 'AgenteReparapp/agregar_producto.html'
    success_url = reverse_lazy('agente:listar_productos')
    success_message = "El Producto fue creado correctamente"


class ActualizarProducto(SuccessMessageMixin, UpdateView):
    model = Producto
    form_class = ProductoForm
    template_name = 'AgenteReparapp/editar_producto.html'
    success_url = reverse_lazy('agente:listar_productos')
    success_message = "El Producto fue modificado correctamente"


class EliminarProducto(SuccessMessageMixin, DeleteView):
    model = Producto
    success_url = reverse_lazy('agente:listar_productos')
    success_message = "El Producto fue eliminado correctamente"

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, self.success_message)
        return super(EliminarProducto, self).delete(request, *args, **kwargs)


class ListadoOrden(ListView):
    model = Orden
    template_name = 'AgenteReparapp/listar_ordenes.html'
    context_object_name = 'ordenes'
    queryset = Orden.objects.exclude(estado = 'CERRADA')

class AgregarOrdenCliente(SuccessMessageMixin, CreateView):
    model = Orden
    form_class = NuevaOrdenClienteForm
    template_name = 'AgenteReparapp/agregar_orden.html'
    success_url = reverse_lazy('agente:listar_ordenes')
    success_message = "La orden fue creada correctamente"

class AgregarOrden(SuccessMessageMixin, CreateView):
    model = Orden
    form_class = NuevaOrdenForm
    template_name = 'AgenteReparapp/agregar_orden.html'
    success_url = reverse_lazy('agente:listar_ordenes')
    success_message = 'La orden fue creada correctamente'

class ActualizarOrden(SuccessMessageMixin, UpdateView):
    model = Orden
    form_class = OrdenForm
    template_name = 'AgenteReparapp/editar_orden.html'
    success_url = reverse_lazy('agente:listar_ordenes')
    success_message = "La orden fue modificada correctamente"

class EliminarOrden(SuccessMessageMixin, DeleteView):
    model = Orden
    success_url = reverse_lazy('agente:listar_ordenes')
    success_message = "La orden fue eliminada correctamente"

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, self.success_message)
        return super(EliminarOrden, self).delete(request, *args, **kwargs)

class ListadoFactura(ListView):
    model = Factura
    template_name = 'AgenteReparapp/listar_facturas.html'
    context_object_name = 'facturas'
    queryset = Factura.objects.all()

class AgregarFactura(SuccessMessageMixin, CreateView):
    model = Factura
    form_class = FacturaForm
    template_name = 'AgenteReparapp/agregar_factura.html'
    success_url = reverse_lazy('agente:listar_facturas')
    success_message = "La factura fue creada correctamente"


class ActualizarFactura(SuccessMessageMixin, UpdateView):
    model = Factura
    form_class = FacturaForm
    template_name = 'AgenteReparapp/editar_factura.html'
    success_url = reverse_lazy('agente:listar_facturas')
    success_message = "La factura fue modificada correctamente"


class EliminarFactura(SuccessMessageMixin, DeleteView):
    model = Factura
    success_url = reverse_lazy('agente:listar_facturas')
    success_message = "La factura fue eliminada correctamente"

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, self.success_message)
        return super(EliminarFactura, self).delete(request, *args, **kwargs)


class Inicio(TemplateView):
    template_name = 'inicio/index.html'


class Consulta(TemplateView):
    template_name = 'inicio/consulta.html'


def consultarOrden(request):
    queryset = request.GET.get('buscar')
    orden= 0
    try:
        if queryset:
            orden = Orden.objects.filter(orden_id=int(queryset))
    except:
        print("No fue posible encontrar la orden")
    return render(request, 'inicio/consulta.html', {'orden': orden})

def listar_ordenes_reparadas(request, id):
    orden =  0
    try:
        if id:
            m_user= Usuario.objects.filter(id = id)
            agente = Agente.objects.filter(user = m_user[0])
            orden = agente[0].orden_set.filter(estado = 'REPARADA')
    except:
        print("No fue posible encontrar la orden")
    return render(request, 'AgenteReparapp/listar_ordenes_reparadas.html', {'ordenes': orden})

def consultar_orden_agente(request):
    queryset = request.GET.get('buscar')
    orden= 0
    try:
        if queryset:
            orden = Orden.objects.filter(orden_id=int(queryset))
    except:
        print("No fue posible encontrar la orden")
    return render(request, 'AgenteReparapp/listar_ordenes_buscadas.html', {'ordenes': orden})

class CrearFactura(CreateView):
    model = Factura
    template_name = 'AgenteReparapp/agregar_factura.html'
    form_class = NuevaFacturaForm
    success_url = reverse_lazy('agente:listar_ordenes')

    def get_form_kwargs(self):
        kwargs = super(CrearFactura, self).get_form_kwargs()
        kwargs.update(self.kwargs)  # self.kwargs contains all url conf params
        return kwargs

class CerrarOrden(UpdateView):
    model = Orden
    form_class = InformarOrdenForm
    template_name = 'AgenteReparapp/cerrar_orden.html'
    success_url = reverse_lazy('agente:listar_ordenes')

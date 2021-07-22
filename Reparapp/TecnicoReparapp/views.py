from django.shortcuts import render, redirect
from django.views.generic import ListView, UpdateView, CreateView, DeleteView, DetailView
from django.urls import reverse_lazy
from .forms import TallerForm, CallCenterForm
from .models import Taller,CallCenter
from AgenteReparapp.models import Factura, Orden
from AdminReparapp.models import TecnicoEspecialista, Usuario
from AgenteReparapp.forms import AgregarTecnicoOrdenForm, InformarOrdenForm, RepararOrdenForm

class ListadoTaller(ListView):
    model = Taller
    template_name = 'TecnicoReparapp/listar_talleres.html'
    context_object_name = 'talleres'
    queryset = Taller.objects.all()

class ActualizarTaller(UpdateView):
    model = Taller
    form_class = TallerForm
    template_name = 'TecnicoReparapp/editar_taller.html'
    success_url = reverse_lazy('tecnico:listar_talleres')

class AgregarTaller(CreateView):
    model = Taller
    form_class = TallerForm
    template_name = 'TecnicoReparapp/agregar_taller.html'
    success_url = reverse_lazy('tecnico:listar_talleres')

class EliminarTaller(DeleteView):
    model = Taller
    success_url = reverse_lazy('tecnico:listar_talleres')

class ListadoCallCenter(ListView):
    model = CallCenter
    template_name = 'TecnicoReparapp/listar_callcenters.html'
    context_object_name = 'callcenter'
    queryset = CallCenter.objects.all()

class ActualizarCallCenter(UpdateView):
    model = CallCenter
    form_class = CallCenterForm
    template_name = 'TecnicoReparapp/editar_callcenter.html'
    success_url = reverse_lazy('tecnico:listar_callcenters')

class AgregarCallCenter(CreateView):
    model = CallCenter
    form_class = CallCenterForm
    template_name = 'TecnicoReparapp/agregar_callcenter.html'
    success_url = reverse_lazy('tecnico:listar_callcenters')

class EliminarCallCenter(DeleteView):
    model = CallCenter
    success_url = reverse_lazy('tecnico:listar_callcenters')

def consultarOrden(request,id):
    orden =  0
    try:
        if id:
            m_user= Usuario.objects.filter(id = id)
            tecnico = TecnicoEspecialista.objects.filter(user = m_user[0])
            orden = tecnico[0].orden_set.all().exclude(estado = 'REPARADA')
    except:
        print("No fue posible encontrar la orden")
    return render(request, 'TecnicoReparapp/mis_ordenes.html', {'ordenes': orden})

class ListadoOrdenes(ListView):
    model = Orden
    template_name = 'TecnicoReparapp/listar_ordenes.html'
    context_object_name = 'ordenes'
    queryset = Orden.objects.exclude(estado='REPARADA').exclude(estado = 'EN REPARACIÓN')

class ActualizarOrden(UpdateView):
    model = Orden
    form_class = AgregarTecnicoOrdenForm
    template_name = 'TecnicoReparapp/editar_orden.html'
    success_url = reverse_lazy('tecnico:listar_ordenes')
    #success_message = "La orden fue modificada correctamente"

class OrdenDetailView(DetailView):
    model = Orden
    template_name = "TecnicoReparapp/detail_orden.html"

class RepararOrden(UpdateView):
    model = Orden
    form_class = RepararOrdenForm
    template_name = 'TecnicoReparapp/reparar_orden.html'
    success_url = reverse_lazy('tecnico:listar_ordenes')

class ListarFacturas(ListView):
    model = Factura
    template_name = 'OperadorReparapp/listar_facturas.html'
    context_object_name = 'facturas'
    queryset = Factura.objects.all()

class EnviarOrden(UpdateView):
    model = Orden
    form_class = InformarOrdenForm
    template_name = 'OperadorReparapp/editar_factura.html'
    success_url = reverse_lazy('tecnico:listar_facturas')
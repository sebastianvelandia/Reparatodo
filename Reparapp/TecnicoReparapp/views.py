from django.shortcuts import render, redirect
from django.views.generic.edit import FormView
from django.views.generic import TemplateView, ListView, UpdateView, CreateView, DeleteView
from django.urls import reverse_lazy
from .forms import TallerForm, CallCenterForm
from .models import Taller,CallCenter

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
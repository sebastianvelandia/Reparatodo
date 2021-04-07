from django.shortcuts import render, redirect
from django.views.generic.edit import FormView
from django.views.generic import TemplateView, ListView, UpdateView, CreateView, DeleteView
from django.urls import reverse_lazy
from .forms import AgenteForm, TecnicoEspecialistaForm, FormularioLogin
from .models import Agente, TecnicoEspecialista

# Create your views here.

class Inicio(TemplateView):
   template_name = 'inicio/index.html'

class Login(FormView):
    template_name = 'inicio/login.html'
    form_class = FormularioLogin
    success_url = reverse_lazy('index')

class ListadoAgente(ListView):
    model = Agente
    template_name = 'AdminReparapp/listar_agentes.html'
    context_object_name = 'agentes'
    queryset = Agente.objects.all()

class ActualizarAgente(UpdateView):
    model = Agente
    form_class = AgenteForm
    template_name = 'AdminReparapp/editar_agente.html'
    success_url = reverse_lazy('my_admin:listar_agentes')

class AgregarAgente(CreateView):
    model = Agente
    form_class = AgenteForm
    template_name = 'AdminReparapp/agregar_agente.html'
    success_url = reverse_lazy('my_admin:listar_agentes')

class EliminarAgente(DeleteView):
    model = Agente
    success_url = reverse_lazy('my_admin:listar_agentes')

class ListadoTecnico(ListView):
    model = TecnicoEspecialista
    template_name = 'AdminReparapp/listar_tecnicos.html'
    context_object_name = 'tecnicos'
    queryset = TecnicoEspecialista.objects.all()

class ActualizarTecnico(UpdateView):
    model = TecnicoEspecialista
    form_class = TecnicoEspecialistaForm
    template_name = 'AdminReparapp/editar_tecnico.html'
    success_url = reverse_lazy('my_admin:listar_tecnicos')

class AgregarTecnico(CreateView):
    model = TecnicoEspecialista
    form_class = TecnicoEspecialistaForm
    template_name = 'AdminReparapp/agregar_tecnico.html'
    success_url = reverse_lazy('my_admin:listar_tecnicos')

class EliminarTecnico(DeleteView):
    model = TecnicoEspecialista
    success_url = reverse_lazy('my_admin:listar_tecnicos')
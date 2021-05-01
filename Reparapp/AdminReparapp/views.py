from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages
from django.db.models import Q
from django.views.generic.edit import FormView
from django.views.generic import TemplateView, ListView, UpdateView, CreateView, DeleteView
from django.views.decorators.cache import never_cache
from django.views.decorators.csrf import csrf_protect
from django.utils.decorators import method_decorator
from django.contrib.auth import login, logout, authenticate
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect
from django.shortcuts import render

# Create your views here.
from .forms import AgenteForm, TecnicoEspecialistaForm, FormularioLogin, EditarForm, AgregarTrabajadorForm, OperadorForm
from .models import Agente, TecnicoEspecialista, Usuario, Operador
from .decorators import allowed_agente


class Inicio(TemplateView):
    template_name = 'inicio/index.html'


def home(request):
    return render(request, 'index.html')

# def listar_trabajadores(request):
#     busqueda = request.GET.get("buscar")
#     trabajadores = Usuario.objects.filter(is_admin='false')

#     if busqueda:
#         Usuario.objects.filter(is_admin = 'false'


#         )


class Login(FormView):
    template_name = 'inicio/login.html'
    form_class = FormularioLogin
    success_url = reverse_lazy('index')

    @method_decorator(csrf_protect)
    @method_decorator(never_cache)
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return HttpResponseRedirect(self.get_success_url())
        else:
            return super(Login, self).dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        login(self.request, form.get_user())
        return super(Login, self).form_valid(form)


def cerrar_sesion(request):
    logout(request)
    return HttpResponseRedirect('/accounts/login/')


class AgregarTrabajador(CreateView):
    model = Usuario
    form_class = AgregarTrabajadorForm
    template_name = 'AdminReparapp/agregar.html'
    success_url = reverse_lazy('my_admin:listar_agentes')


class ListadoAgente(ListView):
    model = Agente
    template_name = 'AdminReparapp/listar_agentes.html'
    context_object_name = 'agentes'
    queryset = Agente.objects.all()


class AgregarAgente(SuccessMessageMixin, CreateView):
    model = Usuario
    form_class = AgenteForm
    template_name = 'AdminReparapp/agregar_agente.html'
    success_url = reverse_lazy('my_admin:listar_agentes')
    success_message = "El Agente fue creado correctamente"


class ActualizarAgente(SuccessMessageMixin, UpdateView):
    model = Usuario
    form_class = EditarForm
    template_name = 'AdminReparapp/editar_agente.html'
    success_url = reverse_lazy('my_admin:listar_agentes')
    success_message = "El Agente fue modificado correctamente"


class EliminarAgente(SuccessMessageMixin, DeleteView):
    model = Usuario
    success_url = reverse_lazy('my_admin:listar_agentes')
    success_message = "El Agente fue eliminado correctamente"
    def delete(self, request, *args, **kwargs):
        messages.success(self.request, self.success_message)
        return super(EliminarAgente, self).delete(request, *args, **kwargs)


class ListadoTecnico(ListView):
    model = TecnicoEspecialista
    template_name = 'AdminReparapp/listar_tecnicos.html'
    context_object_name = 'tecnicos'
    queryset = TecnicoEspecialista.objects.all()


class AgregarTecnico(SuccessMessageMixin, CreateView):
    model = Usuario
    form_class = TecnicoEspecialistaForm
    template_name = 'AdminReparapp/agregar_tecnico.html'
    success_url = reverse_lazy('my_admin:listar_tecnicos')
    success_message = "El Técnico fue creado correctamente"


class ActualizarTecnico(SuccessMessageMixin, UpdateView):
    model = Usuario
    form_class = EditarForm
    template_name = 'AdminReparapp/editar_tecnico.html'
    success_url = reverse_lazy('my_admin:listar_tecnicos')
    success_message = "El Técnico fue modificado correctamente"


class EliminarTecnico(SuccessMessageMixin, DeleteView):
    model = Usuario
    success_url = reverse_lazy('my_admin:listar_tecnicos')
    success_message = "El Técnico fue eliminado correctamente"
    def delete(self, request, *args, **kwargs):
        messages.success(self.request, self.success_message)
        return super(EliminarTecnico, self).delete(request, *args, **kwargs)


class ListadoOperador(ListView):
    model = Operador
    template_name = 'AdminReparapp/listar_operadores.html'
    context_object_name = 'operadores'
    queryset = Operador.objects.all()


class AgregarOperador(SuccessMessageMixin, CreateView):
    model = Usuario
    form_class = OperadorForm
    template_name = 'AdminReparapp/agregar_operador.html'
    success_url = reverse_lazy('my_admin:listar_operadores')
    success_message = "El Operador fue creado satisfactoriamente"


class ActualizarOperador(SuccessMessageMixin, UpdateView):
    model = Usuario
    form_class = EditarForm
    template_name = 'AdminReparapp/editar_operador.html'
    success_url = reverse_lazy('my_admin:listar_operadores')
    success_message = "El Operador fue modificado correctamente"


class EliminarOperador(SuccessMessageMixin, DeleteView):
    model = Usuario
    success_url = reverse_lazy('my_admin:listar_operadores')
    success_message = "El Operador fue eliminado correctamente"
    def delete(self, request, *args, **kwargs):
        messages.success(self.request, self.success_message)
        return super(EliminarOperador, self).delete(request, *args, **kwargs)

# def login_view(request):
#     if request.method == 'POST':
#         form = AuthenticationForm(data=request.POST)
#         if form.is_valid():
#             email = form.cleaned_data.get('username')
#             password = form.cleaned_data.get('password')
#             user = authenticate(email=email, password=password)
#             if user is not None:
#                 login(request,user)
#                 return redirect('index')
#             else:
#                 messages.error(request, 'Correo o contraseña invalida')
#         else:
#             messages.error(request, 'Correo o contraseña invalida')
#     return render(request, 'inicio/login.html',context={'form':AuthenticationForm()})

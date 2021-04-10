from django.views.generic.edit import FormView
from django.views.generic import TemplateView, ListView, UpdateView, CreateView, DeleteView
from django.views.decorators.cache import never_cache
from django.views.decorators.csrf import csrf_protect
from django.utils.decorators import method_decorator
from django.contrib.auth import login, logout, authenticate
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect

# Create your views here.
from .forms import AgenteForm, TecnicoEspecialistaForm, FormularioLogin
from .models import Agente, TecnicoEspecialista, Usuario
from .decorators import allowed_agente

class Inicio(TemplateView):
    template_name = 'inicio/index.html'


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

class ListadoAgente(ListView):
    model = Agente
    template_name = 'AdminReparapp/listar_agentes.html'
    context_object_name = 'agentes'
    queryset = Agente.objects.all()

class ActualizarAgente(UpdateView):
    model = Usuario
    form_class = AgenteForm
    template_name = 'AdminReparapp/editar_agente.html'
    success_url = reverse_lazy('my_admin:listar_agentes')


class AgregarAgente(CreateView):
    model = Usuario
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

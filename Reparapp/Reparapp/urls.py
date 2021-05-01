"""Reparapp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth.decorators import login_required
from AdminReparapp.views import Inicio, Login, cerrar_sesion, home
from AgenteReparapp.views import consultarOrden, Consulta

urlpatterns = [
    path('admin/', admin.site.urls),
    path('my_admin/', include(('AdminReparapp.urls', 'my_admin'))),
    path('agente/', include(('AgenteReparapp.urls', 'agente'))),
    path('tecnico/', include(('TecnicoReparapp.urls', 'tecnico'))),
    path('inicio/', login_required(Inicio.as_view()), name='index'),
    path('accounts/login/', Login.as_view(), name = 'login'),
    path('',home, name = 'home'),
    path('logout/', login_required(cerrar_sesion), name='logout'),
    path('consulta/',Consulta.as_view(),name='consulta' ),
    path('consultar/',consultarOrden,name='consultar')
]

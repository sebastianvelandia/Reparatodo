from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from TecnicoReparapp.models import Taller, CallCenter
# Create your models here.


class Agente(models.Model):
    agente_id = models.CharField(primary_key=True, max_length=50)
    nombre = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    telefono = models.CharField(max_length=20)

    class Meta:
        verbose_name = ("Agente")
        verbose_name_plural = ("Agentes")

    def __str__(self):
        return self.nombre

    def get_absolute_url(self):
        return reverse("Agente_detail", kwargs={"pk": self.pk})


class TecnicoEspecialista(models.Model):
    tecnico_id = models.CharField(primary_key=True, max_length=50)
    nombre = models.CharField(max_length=50)
    telefono = models.CharField(max_length=20)
    password = models.CharField(max_length=50)
    taller = models.ForeignKey(Taller, on_delete=models.CASCADE)

    class Meta:
        verbose_name = ("TecnicoEspecialista")
        verbose_name_plural = ("TecnicosEspecialistas")

    def __str__(self):
        return self.nombre

    def get_absolute_url(self):
        return reverse("TecnicoEspecialista_detail", kwargs={"pk": self.pk})


class Operador(models.Model):
    operador_id = models.CharField(primary_key=True, max_length=50)
    nombre = models.CharField(max_length=50)
    telefono = models.CharField(max_length=20)
    password = models.CharField(max_length=50)
    call_center = models.ForeignKey(CallCenter, on_delete=models.CASCADE)

    class Meta:
        verbose_name = ("Operador")
        verbose_name_plural = ("Operadores")

    def __str__(self):
        return self.nombre

    def get_absolute_url(self):
        return reverse("Operador_detail", kwargs={"pk": self.pk})

from django.db import models
from django.contrib.auth.models import User, AbstractBaseUser, BaseUserManager
from TecnicoReparapp.models import Taller, CallCenter
# Create your models here.


class UsuarioManager(BaseUserManager):
    def create_user(self, email, username, nombres, apellidos, password=None):
        if not email:
            raise ValueError('El usuario debe tener un correo electrónico')

        usuario = self.model(
            username=username,
            email=self.normalize_email(email),
            nombres=nombres,
            apellidos=apellidos
        )
        usuario.set_password(password)
        usuario.save()
        return usuario

    def create_superuser(self, username, email, nombres, apellidos, password):
        usuario = self.create_user(
            email=email,
            username=username,
            nombres=nombres,
            apellidos=apellidos,
            password=password
        )
        usuario.usuario_administrador = True
        usuario.save()
        return usuario


class Usuario(AbstractBaseUser):
    username = models.CharField('Nombre de usuario', unique=True, max_length=50)
    email = models.EmailField('Correo electrónico',unique=True, max_length=254)
    nombres = models.CharField('Nombres', blank=True, null=True, max_length=50)
    apellidos = models.CharField('Apellidos', max_length=50, blank=True, null=True,)
    usuario_activo = models.BooleanField(default=True)
    usuario_administrador = models.BooleanField(default=True)
    usuario_agente = models.BooleanField(default=False)
    usuario_tecnico = models.BooleanField(default=False)
    usuario_operador = models.BooleanField(default=False)
    objects = UsuarioManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email', 'nombres', 'apellidos']

    def __str__(self):
        return self.nombres

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    @property
    def is_staff(self):
        return self.usuario_administrador

    # @property
    def is_agente(self):
        return self.usuario_agente


class Agente(models.Model):
    user = models.OneToOneField(Usuario, on_delete=models.CASCADE, primary_key = True)
    agente_id = models.CharField(max_length=50, unique = True)
    telefono = models.CharField(max_length=20)

    class Meta:
        verbose_name = ("Agente")
        verbose_name_plural = ("Agentes")

    def __str__(self):
        return self.user.nombres

    def get_absolute_url(self):
        return reverse("Agente_detail", kwargs={"pk": self.pk})


class TecnicoEspecialista(models.Model):
    user = models.OneToOneField(Usuario, on_delete=models.CASCADE, primary_key = True)
    tecnico_id = models.CharField(unique=True, max_length=50)
    telefono = models.CharField(max_length=20)
    taller = models.ForeignKey(Taller, on_delete=models.CASCADE)

    class Meta:
        verbose_name = ("TecnicoEspecialista")
        verbose_name_plural = ("TecnicosEspecialistas")

    def __str__(self):
        return self.user.nombres

    def get_absolute_url(self):
        return reverse("TecnicoEspecialista_detail", kwargs={"pk": self.pk})


class Operador(models.Model):
    user = models.OneToOneField(Usuario, on_delete=models.CASCADE, primary_key = True)
    operador_id = models.CharField(max_length=50, unique=True)
    telefono = models.CharField(max_length=20)
    call_center = models.ForeignKey(CallCenter, on_delete=models.CASCADE)

    class Meta:
        verbose_name = ("Operador")
        verbose_name_plural = ("Operadores")

    def __str__(self):
        return self.user.nombres

    def get_absolute_url(self):
        return reverse("Operador_detail", kwargs={"pk": self.pk})

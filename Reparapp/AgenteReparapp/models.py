from django.db import models
from AdminReparapp.models import Agente, TecnicoEspecialista
from TecnicoReparapp.models import CallCenter

# Create your models here.
REPARADA = 'REPARADA'
RECEPCIONADA = 'RECEPCIONADA'
EN_REPARACION = 'EN REPARACIÓN'
INFORMADA = 'INFORMADA'
CERRADA = 'CERRADA'
ESTADOS = (
    (REPARADA, 'Reparado'),
    (RECEPCIONADA, 'Recepcionado'),
    (EN_REPARACION, 'En Reparación'),
    (INFORMADA, 'Informada'),
    (CERRADA, 'Cerrada'),
)

class Cliente(models.Model):
    cliente_id = models.CharField(primary_key=True, max_length=50)
    nombre = models.CharField(max_length=50)
    telefono = models.CharField(max_length=10)

    class Meta:
        verbose_name = ("Cliente")
        verbose_name_plural = ("Clientes")

    def __str__(self):
        return self.nombre

    def get_absolute_url(self):
        reverse("Cliente_detail", kwargs={"pk": self.pk})

class Producto(models.Model):
    codigo_id = models.AutoField(primary_key=True)
    averia = models.TextField()
    nombre_electrodomestico = models.CharField(max_length=50)

    class Meta:
        verbose_name = ("Producto")
        verbose_name_plural = ("Productos")

    def __str__(self):
        return self.nombre_electrodomestico

    def get_absolute_url(self):
        return reverse("Producto_detail", kwargs={"pk": self.pk})

class Orden(models.Model):
    orden_id = models.AutoField(primary_key=True)
    observaciones = models.TextField()
    estado = models.CharField(max_length=20, choices=ESTADOS, default=RECEPCIONADA)
    agente = models.ForeignKey(Agente, on_delete=models.CASCADE)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    tecnico_epecialista = models.ForeignKey(TecnicoEspecialista, on_delete=models.CASCADE, null=True)
    producto = models.OneToOneField(Producto, on_delete=models.CASCADE)
    fecha_ingreso = models.DateField(auto_now_add=True)

    class Meta:
        verbose_name = ("Orden")
        verbose_name_plural = ("Ordenes")

    def __str__(self):
        return self.orden_id

    def get_absolute_url(self):
        return reverse("Orden_detail", kwargs={"pk": self.pk})

class Factura(models.Model):
    factura_id = models.AutoField(primary_key=True)
    costo_orden = models.IntegerField()
    orden = models.OneToOneField(Orden, on_delete=models.CASCADE)
    agente = models.ForeignKey(Agente, on_delete=models.CASCADE)
    callCenter = models.ForeignKey(CallCenter, on_delete=models.CASCADE)
    fecha_retiro = models.DateField(auto_now_add=False)

    class Meta:
        verbose_name = ("Factura")
        verbose_name_plural = ("Facturas")

    def __str__(self):
        return self.Factura_id

    def get_absolute_url(self):
        return reverse("Factura_detail", kwargs={"pk": self.pk})

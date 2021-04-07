from django.db import models

# Create your models here.
class Taller(models.Model):
    Taller_id = models.AutoField(primary_key = True)
    Nombre_taller = models.CharField(max_length=50)
    class Meta:
        verbose_name = ("Taller")
        verbose_name_plural = ("Tallers")

    def __str__(self):
        return self.Nombre_taller

    def get_absolute_url(self):
        return reverse("Taller_detail", kwargs={"pk": self.pk})

class CallCenter(models.Model):
    CallCenter_NIT= models.CharField(primary_key=True,max_length=50)
    Nombre_callcenter = models.CharField(max_length=50)
    Direccion = models.CharField(max_length=50)

    class Meta:
        verbose_name = ("CallCenter")
        verbose_name_plural = ("CallCenters")

    def __str__(self):
        return self.Nombre_callcenter

    def get_absolute_url(self):
        return reverse("CallCenter_detail", kwargs={"pk": self.pk})


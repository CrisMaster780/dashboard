from django.db import models

class UnidadMedida(models.Model):
    descripcion = models.CharField(max_length=250)
    resumido = models.CharField(max_length=10)
    estado = models.BooleanField(default=True, blank=True, null=True)
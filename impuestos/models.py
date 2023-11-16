from django.db import models

class Impuestos(models.Model):
    descripcion = models.CharField(max_length=250)
    porcentaje = models.PositiveIntegerField()
    estado = models.BooleanField(default=True, blank=True, null=True)
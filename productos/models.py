from django.db import models
from impuestos.models import Impuestos
from unidad_medida.models import UnidadMedida

class Clasificacion(models.Model):
    descripcion = models.CharField(max_length=240)
    estado = models.BooleanField(default=True, blank=True, null=True)

class Marca(models.Model):
    descripcion = models.CharField(max_length=240)
    estado = models.BooleanField(default=True, blank=True, null=True)



class Productos(models.Model):
    descripcion = models.CharField(max_length=250) 
    codigo_barra = models.CharField(max_length=250,null=True, blank=True, unique=True )
    codigo_producto = models.CharField(max_length=250, null=True, blank=True, unique=True)
    lote = models.CharField(max_length=250, null=True, blank=True)
    precio_costo = models.FloatField()
    precio_venta = models.FloatField()
    precio_mayorista = models.FloatField() 
    existencia = models.FloatField(null=True, blank=True)
    fecha_hora_registro = models.DateTimeField(auto_now=True, null=True, blank=True)
    vencimiento = models.DateTimeField(null=True, blank=True)
    estado = models.BooleanField(default=True, blank=True, null=True)
    marca = models.ForeignKey(Marca, on_delete=models.PROTECT)
    clasificacion = models.ForeignKey(Clasificacion, on_delete=models.PROTECT)
    impuesto = models.ForeignKey(Impuestos, on_delete=models.PROTECT)
    unidad_medida = models.ForeignKey(UnidadMedida, on_delete=models.PROTECT)


    def __str__(self):
        return self.descripcion



from django.contrib import admin
from django.urls import path, include
from .views import pedido_venta

urlpatterns = [
    path("", pedido_venta, name="pedido_venta"),
   
   
]
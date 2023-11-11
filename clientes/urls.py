from django.contrib import admin
from django.urls import path, include
from .views import lista_clientes, nuevo_cliente, modificar_cliente, eliminar_cliente

urlpatterns = [
    path("", lista_clientes, name="lista_clientes"),
    path("nuevo_cliente", nuevo_cliente, name="nuevo_cliente"),
    path("modificar_cliente/<int:cliente_id>/", modificar_cliente, name="modificar_cliente"),
     path("eliminar_cliente/<int:cliente_id>/", eliminar_cliente, name="eliminar_cliente"),
]

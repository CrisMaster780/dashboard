from django.contrib import admin
from django.urls import path, include
from .views import lista_productos, nuevo_producto, modificar_producto, eliminar_producto

urlpatterns = [
    path("", lista_productos, name="lista_productos"),
    path("nuevo_producto", nuevo_producto, name="nuevo_producto"),
    path("modificar_producto/<int:id_prod>/", modificar_producto, name="modificar_producto"),
    path("eliminar_producto/<int:id_prod>/", eliminar_producto, name="eliminar_producto"),

   
]
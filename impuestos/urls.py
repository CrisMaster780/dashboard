from django.contrib import admin
from django.urls import path, include
from .views import lista_impuesto, nuevo_impuesto, modificar_impuesto, eliminar_impuesto

urlpatterns = [
    path("", lista_impuesto, name="lista_impuesto"),
    path("nuevo_impuesto", nuevo_impuesto, name="nuevo_impuesto"),
    path("modificar_impuesto/<int:id_unidad>/", modificar_impuesto, name="modificar_impuesto"),
    path("eliminar_impuesto/<int:id_imp>/", eliminar_impuesto, name="eliminar_impuesto"),
]
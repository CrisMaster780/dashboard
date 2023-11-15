from django.contrib import admin
from django.urls import path, include
from .views import lista_unidad, nueva_unidad, modificar_uniadad, eliminar_unidad

urlpatterns = [
    path("", lista_unidad, name="lista_unidad"),
    path("nueva_uniad_medida", nueva_unidad, name="nueva_uniad_medida"),
    path("modificar_uniadad/<int:id_unidad>/", modificar_uniadad, name="modificar_uniadad"),
    path("eliminar_unidad/<int:id_unidad>/", eliminar_unidad, name="eliminar_unidad"),
]
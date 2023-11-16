from django.shortcuts import render, redirect
from .models import UnidadMedida
from .form import UnidadMedidaForms
from django.contrib import messages

def lista_unidad(request):
    if request.method == "GET":
        unidades = UnidadMedida.objects.all()
        template_ = "unidad_medida.html"
        context = {"titulo": "Lista de Unidades de Medida", "unidades": unidades}

    return render(request, template_name=template_, context=context)


def nueva_unidad(request):
    if request.method == "GET":
        template_ = "nueva_unidad.html"
        form = UnidadMedidaForms()
        context = {"titulo": "Nueva Unidad de Medida", "form": form}
    else:
        form = UnidadMedidaForms(request.POST)
        if form.is_valid:
            form.save()
            messages.success(request, 'Unidad de Medida guardada exitosamente.')

            return redirect('lista_unidad')
        else:
            messages.error(request, 'Error al guardar la Unidad de Medida.')
            return redirect('lista_unidad')


    return render(request, template_name=template_, context=context)

def modificar_uniadad(request, id_unidad):
    uniadad_instance = UnidadMedida.objects.get(id = id_unidad)
    if request.method == 'GET':
        template_ = "nueva_unidad.html"
        form = UnidadMedidaForms(instance= uniadad_instance)
        context = {"titulo": "Modificar Uniadad de Medida", "form": form}
    else:
        form = UnidadMedidaForms(request.POST, instance=uniadad_instance)
        if form.is_valid:
            form.save()
            messages.success(request, 'Unidad de Medida Modificada exitosamente.')
            return redirect('lista_unidad')
        else:
            messages.error(request, 'Error al Modificar la Unidad de Medida.')
            return redirect('nueva_unidad')


    return render(request, template_name=template_, context=context)

def eliminar_unidad(request, id_unidad):
    unidad_instance = UnidadMedida.objects.get(id = id_unidad)
    unidad_instance.delete()
    messages.success(request, 'Eliminado Exitoso.')
    return redirect('lista_unidad')
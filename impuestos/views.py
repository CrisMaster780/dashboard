from django.shortcuts import render, redirect
from .models import Impuestos
from .form import ImpuestosForms
from django.contrib import messages

def lista_impuesto(request):
    if request.method == "GET":
        impuestos = Impuestos.objects.all()
        template_ = "impuesto.html"
        context = {"titulo": "Lista de Impuestos", "impuestos": impuestos}

    return render(request, template_name=template_, context=context)


def nuevo_impuesto(request):
    if request.method == "GET":
        template_ = "nuevo_impuesto.html"
        form = ImpuestosForms()
        context = {"titulo": "Nuevo Impuesto", "form": form}
    else:
        form = ImpuestosForms(request.POST)
        if form.is_valid:
            form.save()
            messages.success(request, 'Impuesto Guardado exitosamente.')

            return redirect('lista_impuesto')
        else:
            messages.error(request, 'Error al guardar la Impuestos')
            return redirect('lista_impuesto')


    return render(request, template_name=template_, context=context)

def modificar_impuesto(request, id_unidad):
    impuesto_instance = Impuestos.objects.get(id = id_unidad)
    if request.method == 'GET':
        template_ = "nuevo_impuesto.html"
        form = ImpuestosForms(instance= impuesto_instance)
        context = {"titulo": "Modificar Uniadad de Medida", "form": form}
    else:
        form = ImpuestosForms(request.POST, instance=impuesto_instance)
        if form.is_valid:
            form.save()
            messages.success(request, 'Impuesto Modificado exitosamente.')
            return redirect('lista_impuesto')
        else:
            messages.error(request, 'Error al Modificar  Impuestos')
            return redirect('nuevo_impuesto')


    return render(request, template_name=template_, context=context)

def eliminar_impuesto(request, id_imp):
    impuesto_instance = Impuestos.objects.get(id = id_imp)
    impuesto_instance.delete()
    messages.success(request, 'Eliminado Exitoso.')
    return redirect('lista_impuesto')
from django.shortcuts import render, redirect
from .models import Clientes
from .form import ClientesForms
from django.contrib import messages


mensaje = ''
def lista_clientes(request):
    if request.method == "GET":
        clientes = Clientes.objects.all()
        template_ = "clientes.html"
        context = {"titulo": "Lista de Clientes", "clientes": clientes}

    return render(request, template_name=template_, context=context)


def nuevo_cliente(request):

    if request.method == "GET":
        template_ = "nuevo_cliente.html"
        form = ClientesForms()
        context = {"titulo": "Nuevo Cliente", "form": form}
    else:
        form = ClientesForms(request.POST)
        if form.is_valid:
            form.save()
            messages.success(request, 'Cliente guardado exitosamente.')

            return redirect('lista_clientes')
        else:
            messages.error(request, 'Error al guardar el cliente.')
            return redirect('nuevo_cliente')


    return render(request, template_name=template_, context=context)

def modificar_cliente(request, cliente_id):
    cliente_instance = Clientes.objects.get(id = cliente_id)
    if request.method == 'GET':
        template_ = "nuevo_cliente.html"
        form = ClientesForms(instance= cliente_instance)
        context = {"titulo": "Modificar Cliente", "form": form}
    else:
        form = ClientesForms(request.POST, instance=cliente_instance)
        if form.is_valid:
            form.save()
            messages.success(request, 'Cliente Modificado exitosamente.')
            return redirect('lista_clientes')
        else:
            messages.error(request, 'Error al Modificar el cliente.')
            return redirect('nuevo_cliente')


    return render(request, template_name=template_, context=context)


def eliminar_cliente(request, cliente_id):
    cliente_instance = Clientes.objects.get(id = cliente_id)
    cliente_instance.delete()
    messages.success(request, 'Eliminado Exitoso.')
    return redirect('lista_clientes')




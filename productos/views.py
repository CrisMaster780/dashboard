from django.shortcuts import render, redirect
from .models import Productos, Clasificacion, Marca
from .form import ProductosForms
from django.contrib import messages


def lista_productos(request):
    if request.method == "GET":
        productos = Productos.objects.all()
        template_ = "productos.html"
        context = {"titulo": "Lista de Productos", "productos": productos}

    return render(request, template_name=template_, context=context)


def nuevo_producto(request):
    if request.method == "GET":
        template_ = "nuevo_producto.html"
        form = ProductosForms()
        context = {"titulo": "Nuevo Producto", "form": form}
    else:
        form = ProductosForms(request.POST)
        if form.is_valid:
            try:
                form.save()
                messages.success(request, 'Producto Guardado exitosamente.')
                return redirect('lista_productos')
            except:
                messages.error(request, 'Error al guardar la Producto el Producto ya Existe')
                return redirect('lista_productos')
        

        else:
            messages.error(request, 'Error al guardar la Producto')
            return redirect('lista_productos')


    return render(request, template_name=template_, context=context)

def modificar_producto(request, id_prod):
    producto_instance = Productos.objects.get(id = id_prod)
    if request.method == 'GET':
        template_ = "nuevo_producto.html"
        form = ProductosForms(instance= producto_instance)
        context = {"titulo": "Modificar Producto", "form": form}
    else:
        form = ProductosForms(request.POST, instance=producto_instance)
        if form.is_valid:
            form.save()
            messages.success(request, 'Producto Modificado exitosamente.')
            return redirect('lista_productos')
        else:
            messages.error(request, 'Error al Modificar  Productos')
            return redirect('nuevo_producto')
    return render(request, template_name=template_, context=context)



def eliminar_producto(request, id_prod):
    producto_instance = Productos.objects.get(id = id_prod)
    producto_instance.delete()
    messages.success(request, 'Eliminado Exitoso.')
    return redirect('lista_productos')
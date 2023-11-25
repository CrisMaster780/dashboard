from clientes.models import Clientes
from productos.models  import Productos
from django.contrib import messages
from django.shortcuts import render, redirect


def pedidoventa(request):
    if request.method == 'GET':
        productos = Productos.objects.all()
        cliente = Clientes.objects.all()

        template_name = 'pedido_venta.html'
        context = {
            'titulo': 'Pedido Venta',
            'cliente': cliente,
            'productos': productos
        }

    return render(request, template_name, context)
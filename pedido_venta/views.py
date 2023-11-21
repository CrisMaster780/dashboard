from django.shortcuts import render
from clientes.models import Clientes
from django.contrib import messages


def pedido_venta(request):
    if request.method == 'GET':
        cliente = request.GET.get('cliente')
        if cliente :
            cliente_instance = Clientes.objects.filter(documento__icontains=cliente).values(
                'nombre',
                'apellido',
                'documento',
                'direccion',
                'telefono'
            )

            if not cliente_instance:
                messages.warning(request,'No se encontro el cliente')
            else:
                cliente_instance = cliente_instance[0]
            

        else:
            cliente_instance = []
        
        print(cliente_instance)
        template_name = 'pedido_venta.html'
        context = {
            'titulo' : 'Pedido de Venta',
            'cliente': cliente_instance
        }

        return render(request, template_name= template_name, context=context)
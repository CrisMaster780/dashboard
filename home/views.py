from django.shortcuts import render

def index(request):
    template_ = 'index.html'
    context = {
        'titulo': 'Sistema de Gestion'
    }
    return render(request, template_name=template_, context=context)
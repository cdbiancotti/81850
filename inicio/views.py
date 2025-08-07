from django.shortcuts import render, redirect
from django.http import HttpResponse
from inicio.models import Auto
from inicio.forms import FormularioCrearAuto

def inicio(request):
    
    return render(request, 'inicio.html')
    
    # return HttpResponse('<h1>ESTA ES LA PAGINA DE INICIO</h1>')

# v1
# def crear_auto(request, marca, modelo):
    
    
#     auto = Auto(marca=marca, modelo=modelo)
#     auto.save()
    
#     return render(request, 'crear_auto_v1.html', {'auto': auto})

# v2
def crear_auto(request):
    
    
    print(request.POST)
    
    if request.method == "POST":
        formulario = FormularioCrearAuto(request.POST)
        if formulario.is_valid():
            info = formulario.cleaned_data

            auto = Auto(marca=info.get('marca'), modelo=info.get('modelo'))
            auto.save()
        
            return redirect('listado_de_autos')
    else:
        formulario = FormularioCrearAuto()
        
    return render(request, 'crear_auto_v2.html', {'formulario': formulario})

def listado_de_autos(request):

    autos = Auto.objects.all()
    
    return render(request, 'listado_de_autos.html', {'autos': autos})
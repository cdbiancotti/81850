from django.shortcuts import render, redirect
from django.http import HttpResponse
from inicio.models import Auto
from inicio.forms import FormularioCrearAuto, FormularioBuscarAuto
from django.views.generic.edit import DeleteView, UpdateView
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

def inicio(request):
    
    return render(request, 'inicio.html')
    
    # return HttpResponse('<h1>ESTA ES LA PAGINA DE INICIO</h1>')

# v1
# def crear_auto(request, marca, modelo):
    
    
#     auto = Auto(marca=marca, modelo=modelo)
#     auto.save()
    
#     return render(request, 'crear_auto_v1.html', {'auto': auto})

# v2
@login_required
def crear_auto(request):
    
    
    print(request.POST)
    
    if request.method == "POST":
        formulario = FormularioCrearAuto(request.POST, request.FILES)
        if formulario.is_valid():
            info = formulario.cleaned_data

            auto = Auto(marca=info.get('marca'), modelo=info.get('modelo'), imagen=info.get('imagen'))
            auto.save()
        
            return redirect('listado_de_autos')
    else:
        formulario = FormularioCrearAuto()
        
    return render(request, 'crear_auto_v2.html', {'formulario': formulario})

def listado_de_autos(request):

    formulario = FormularioBuscarAuto(request.GET)
    if formulario.is_valid():
        marca_a_buscar = formulario.cleaned_data['marca']
        modelo_a_buscar = formulario.cleaned_data['modelo']
        autos_buscados = Auto.objects.filter(marca__icontains=marca_a_buscar, modelo__icontains=modelo_a_buscar)
    # else:
    #     autos_buscados = Auto.objects.all()
    
    return render(request, 'listado_de_autos.html', {'autos_buscados': autos_buscados, 'formulario': formulario})


def auto_detalle(request, id_auto):
    auto = Auto.objects.get(id=id_auto)
    return render(request, 'auto_detalle.html', {'auto': auto})


# def auto_borrado(request, id_auto):
#     auto = Auto.objects.get(id=id_auto)
#     auto.delete()
#     return render(request, 'auto_detalle.html', {'auto': auto})

class AutoBorrar(LoginRequiredMixin, DeleteView):
    model = Auto
    template_name = "auto_borrar.html"
    success_url = reverse_lazy('listado_de_autos')


class AutoActualizar(LoginRequiredMixin, UpdateView):
    model = Auto
    template_name = "auto_actualizar.html"
    success_url = reverse_lazy('listado_de_autos')
    # fields = ['marca']
    # fields = ['marca', 'modelo']
    fields = '__all__'
    


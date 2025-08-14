from django import forms


class FormularioBaseAuto(forms.Form):
    marca = forms.CharField(max_length=20)
    
class FormularioCrearAuto(FormularioBaseAuto):
    modelo = forms.CharField(max_length=20)
    

class FormularioBuscarAuto(FormularioBaseAuto): 
    marca = forms.CharField(max_length=20, required=False)
    modelo = forms.CharField(max_length=20, required=False)
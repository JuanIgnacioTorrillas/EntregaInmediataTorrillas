from django import forms

#Aca Van Formularios

class PizzaForm(forms.Form):
    
    gusto=forms.CharField(max_length=100)
    porciones=forms.IntegerField()
    estilo=forms.CharField(max_length=100)
    

class MilanesaForm(forms.Form):
    
    tipo_de_relleno=forms.CharField(max_length=100)
    coccion=forms.CharField(max_length=100)
    cantidad=forms.IntegerField()
    acompañamiento=forms.CharField(max_length=100)
    
    
class CervezaForm(forms.Form):
    
    tipo=forms.CharField(max_length=100)
    cantidad_bebible=forms.IntegerField()
    marca=forms.CharField(max_length=100)
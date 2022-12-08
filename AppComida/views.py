from django.shortcuts import render
from AppComida.models import Pizza,Milanesa,Cerveza
from django.http import HttpResponse
from AppComida.forms import PizzaForm,CervezaForm,MilanesaForm

def inicio(request):
    return render (request, "inicio.html")

def pizza(request): #Formulario, Agregar a BD

    if request.method=="POST":
        form=PizzaForm(request.POST) #request,data=request.POST
        if form.is_valid():
            
            #gust=form.cleaned_data_get("gusto")
            #porc=form.cleaned_data_get("porciones")
            #esti=form.cleaned_data_get("estilo")
            #form.save()
            
            informacion=form.cleaned_data
            
            pizza= Pizza(gusto=informacion["gusto"], porciones=informacion["porciones"], estilo=informacion["estilo"])
            pizza.save()
            
            return render (request, "inicio.html", {"mensaje": "Tu Pizza fue Guardada!!!"})
        else:
            return render (request, "pizza.html", {"form":formulario})
        
    else:
        formulario=PizzaForm()
        
    return render (request, "pizza.html", {"form":formulario})

def cerveza(request): #Formulario, Agregar a BD

    if request.method=="POST":
        form=CervezaForm(request.POST)
        if form.is_valid():
            informacion=form.cleaned_data
            tipo=informacion["tipo"]
            cantidad=informacion["cantidad"]
            marca=informacion["marca"]
            cerveza= Cerveza(tipo=tipo, cantidad=cantidad, marca=marca)
            cerveza.save()
            return render (request, "inicio.html", {"mensaje": "Cerveza fue Guardada!!!"})
    else:
        formulario=CervezaForm()
        
    return render (request, "cerveza.html", {"form":formulario})

def milanesa(request): #Formulario, Agregar a BD

    if request.method=="POST":
        form=MilanesaForm(request.POST)
        if form.is_valid():
            informacion=form.cleaned_data
            tipo_de_relleno=informacion["relleno"]
            coccion=informacion["coccion"]
            cantidad=informacion["cantidad"]
            acompañamiento=informacion["acompañamiento"]
            milanesa= Milanesa(tipo_de_relleno=tipo_de_relleno, coccion=coccion, cantidad=cantidad, acompañamiento=acompañamiento)
            milanesa.save()
            return render (request, "inicio.html", {"mensaje": "Tu Milanesa fue Guardada!!!"})
    else:
        formulario=PizzaForm()
        
    return render (request, "milanesa.html", {"form":formulario})


def busquedaPizza(request):
    return render(request, "busqueda_pizza.html")

    
    
def buscar(request):
    
    if request.GET.get("gusto"): #o tambien if "gusto" in request.GET

        gusto=request.GET["gusto"]
        
        Pizzas = Pizza.objects.filter(gusto = gusto)  
        
        return render(request, "resultadobusqueda.html", {'Pizzas': Pizzas })
    else:
        return render(request, "busqueda_pizza.html", {"mensaje":" ¡Vuelva a intentarlo!"})
from django.urls import path
from AppComida.views import *

urlpatterns = [  #1ro comando web 2do views 3ro nombre

path("",inicio,name="inicio"),
path("pizza/",pizza,name="pizza"),
path("milanesa/",milanesa,name="milanesa"),
path("cerveza/",cerveza,name="cerveza"),
path("buscar/", buscar, name="buscar"),
path("busquedaPizza/", buscar, name="busquedaPizza"),
]
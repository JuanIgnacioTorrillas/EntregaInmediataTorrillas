from django.db import models


#ACA VAN LAS CLASES
 
class Pizza (models.Model):
    
    gusto=models.CharField(max_length=100) #STR
    porciones=models.IntegerField() #INT
    estilo=models.CharField(max_length=100) #STR

    def __str__(self):
        return "Mi pizza ideal: " +self.gusto+" "+self.porciones+" "+self.estilo
    
    
class Milanesa (models.Model):
    
    tipo_de_relleno=models.CharField(max_length=100)
    coccion=models.CharField(max_length=100)
    cantidad=models.IntegerField()
    acompañamiento=models.CharField(max_length=100)
    
    def __str__(self):
        return "Milanesa de: " +self.tipo_de_relleno+" con, "+self.acompañamiento+".Dame, "+self.cantidad

class Cerveza (models.Model):
    
    tipo=models.CharField(max_length=100)
    cantidad_bebible=models.IntegerField()
    marca=models.CharField(max_length=100)
    
    def __str__(self):
        return "Soy fan de la cerveza " +self.tipo_de_cerveza+", de la marca: "+self.marca
    
    
    
    
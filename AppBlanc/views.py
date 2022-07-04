from django.shortcuts import render
from AppBlanc.models import Familiares
from django.http import HttpResponse
from django.template import Context, Template, loader #para el templateBlanc
# Create your views here.
def padre(self):
    padre= Familiares(nombre='Jorge Blanc', fecha_nacimiento='1946-6-25', edad=76, tiene_hijos=True) 
    #DateField es YYYY-MM-DD. esta ok llamarlo padre aca? o tiene q ser familiar??
    padre.save()
    texto=f'Familiar es mi Padre, {padre.nombre}, nacio el {padre.fecha_nacimiento}. Tiene {padre.edad} anios. Tiene hijos:{padre.tiene_hijos}'
    return HttpResponse(texto)

def abuelo_mat(self):
    abuelo_mat= Familiares(nombre='Juan Lock', fecha_nacimiento='1915-2-03', edad=100, tiene_hijos=True) 
    #DateField es YYYY-MM-DD. 
    abuelo_mat.save()
    texto=f'Familiar es mi abuelo materno, {abuelo_mat.nombre}, nacio el {abuelo_mat.fecha_nacimiento}. Tiene {abuelo_mat.edad} anios. Tiene hijos:{abuelo_mat.tiene_hijos}'
    return HttpResponse(texto)

def hermana(self):
    hermana= Familiares(nombre='carmen', fecha_nacimiento='1982-2-03', edad=40, tiene_hijos=False) 
    hermana.save()
    texto=f'Familiar es mi hemana, {hermana.nombre}, nacio el {hermana.fecha_nacimiento}. Tiene {hermana.edad} anios. Tiene hijos:{hermana.tiene_hijos}'
    return HttpResponse(texto)

def plantilla(self):
    plantilla=loader.get_template('templateBlanc.html')
    documento=plantilla.render() #que meto adentro del render? lo q tenga en body?
    return HttpResponse(documento)


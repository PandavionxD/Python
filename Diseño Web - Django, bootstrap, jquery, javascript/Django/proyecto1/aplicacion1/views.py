from django.shortcuts import render
from django.http import HttpResponse
from aplicacion1.models import Web
from django import forms


# Create your views here.
def vista1(request):
    return HttpResponse('Buenos dias!')

def vista2(request):
    return HttpResponse('Adios, hasta la proxima.')
def vista3(request):
    diccionario = {'etiqueta':'Este es el valor de la etiqueta, saludo desde django'}
    return render(request,'aplicacion1/index1.html',context=diccionario)

def vista4(request):
    diccionario = {}
    return render(request,'aplicacion1/index2.html',context=diccionario)

def vista5(request):
    lista_webs = Web.objects.order_by('nombre')
    diccionario = {'lista_webs':lista_webs}
    return render(request,'aplicacion1/portada.html',context=diccionario)

def forms(request):
    formulario = forms.Formulario()
    diccionario = {'formulario':formulario}
    return render(request,'aplicacion1/formulario.html',context=diccionario)

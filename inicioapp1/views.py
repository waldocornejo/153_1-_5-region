from django.shortcuts import render

# Create your views here.

def primera(request):
    return render (request,'inicioapp1/archivo.html')

def solucion2(request):
    return render (request,'inicioapp1/solucion2.html')
    
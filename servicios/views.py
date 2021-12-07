

# Create your views here.

from django.shortcuts import render

def servicios(request):
    return render(request, "servicios/servicios.html")

def constancia(request):
    return render(request, "servicios/constancia.html")

def kardex(request):
    return render(request, "servicios/kardex.html")

def seguro(request):
    return render(request, "servicios/seguro.html")

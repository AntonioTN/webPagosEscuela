from django.shortcuts import render, redirect
from .models import Alumnos
from .forms import AlumnosForm


def alumnos(request):
    alumno = Alumnos.objects.all()
    context = {'Alumnos':alumno}
    return render(request, "alumnos/alumnos.html", context)
    

def agregar(request):
    if request.method == "POST":
        form = AlumnosForm(request.POST)
        if form. is_valid():
            form.save()
            return redirect('alumnos')
    else:
        form = AlumnosForm()

    context = {'form' : form}
    return render(request, 'alumnos/agregar.html', context)

def eliminar(request, alumno_id):
    alumno = Alumnos.objects.get(id=alumno_id)
    alumno.delete()
    return redirect("alumnos")

def editar(request, alumno_id):
    alumno = Alumnos.objects.get(id=alumno_id)
    if request.method == "POST":
        form = AlumnosForm(request.POST, instance=alumno)
        if form. is_valid():
            form.save()
            return redirect("alumnos")
    else:
        form = AlumnosForm(instance=alumno)
        
    context = {"form" : form }
    return render(request, "alumnos/editar.html", context)


# def registro_pagos(request):
#     # alumno = Alumnos.objects.all()
#     # context = {'Alumnos':alumno}
#     return render(request, "alumnos/registro_pagos.html")
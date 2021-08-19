from django.shortcuts import render

def pagos(request):
    return render(request, "pagos/pagos.html")

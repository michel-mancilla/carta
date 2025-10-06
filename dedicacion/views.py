from django.shortcuts import render

def inicio(request):
    return render(request, 'dedicacion/inicio.html')

def carta_secreta(request):
    return render(request, 'dedicacion/carta.html')

def nuestros_recuerdos(request):
    return render(request, 'dedicacion/recuerdos.html')

def mi_amor(request):
    return render(request, 'dedicacion/amor.html')

def palabras_especiales(request):
    return render(request, 'dedicacion/palabras.html')
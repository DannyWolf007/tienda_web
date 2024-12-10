from django.shortcuts import render

def index(request):
    return render(request, 'index.html') 

def trajes(request):
    return render(request, 'trajes.html')  

def tenis(request):
    return render(request, 'tenis.html')

def playeras(request):
    return render(request, 'playeras.html')

def pantalones(request):
    return render(request, 'pantalones.html')

def lentes(request):
    return render(request, 'lentes.html')

def chumpas(request):
    return render(request, 'chumpas.html')

def descuentos(request):
    return render(request, 'descuentos.html')

def accesorios(request):
    return render(request, 'accesorios.html')

def registro(request):
    return render(request, 'registro.html')


def carrito(request):
    return render(request, 'carrito.html')
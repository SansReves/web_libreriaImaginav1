from django.shortcuts import render
from .models import Libro


def iniciosesion(request):
    return render(request,'core/iniciosesion.html')

def home(request):
    return render(request,'core/home.html')

def catalogo(request):
    libros = Libro.objects.all()
    data = {
        'libros' : libros

    }
    return render(request,'core/catalogo.html',data)

def servicios(request):
    return render(request,'core/servicios.html')

def quienessomos(request):
    return render(request,'core/quienessomos.html')

def home(request):
    return render(request,'core/home.html')

def seguimiento(request):
    return render(request,'core/seguimiento.html')



from django.shortcuts import render


def iniciosesion(request):
    return render(request,'core/iniciosesion.html')

def home(request):
    return render(request,'core/home.html')



from django.shortcuts import render
from .models import Animal
def index(request):
    listaAnimais = Animal.objects.filter(adotado=False)
    return render(request, 'index.html',{'animais':listaAnimais})

def listaAnimais(request):
    listaAnimais = Animal.objects.filter(adotado=False)
    return render(request, 'listaAnimais.html',{'animais':listaAnimais})
from django.shortcuts import render
from .models import Animal
def index(request):
    return render(request, 'index.html')
def listaAnimais(request):
    listaAnimais = Animal.objects.filter(adotado=False)
    return render(request, 'listaAnimais.html',{'animais':listaAnimais})
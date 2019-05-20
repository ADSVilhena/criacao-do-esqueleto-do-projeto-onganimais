from django.shortcuts import render
from .models import Animal


def index(request):
    listaAnimais = Animal.objects.filter(adotado=False)
    return render(request, 'index.html',{'animais':listaAnimais})

def listaAnimais(request):
    listaAnimais = Animal.objects.filter(adotado=False)
    return render(request, 'listaAnimais.html',{'animais':listaAnimais})

def teste(request):
    listaAnimais = Animal.objects.filter(adotado=False)
    return render(request, 'descricao.html',{'animais':listaAnimais})





def home(request):
    animais = Animal.objects.all()
    paginator = Paginator(animais, 12)
    page = request.GET.get('page')
    animais = paginator.get_page(page)
    return render(request, 'adocao/index.html', {'animais':animais})


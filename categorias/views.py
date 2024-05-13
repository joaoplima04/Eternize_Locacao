from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request, 'categorias/index.html')

def guardanapos(request):
    return render(request, 'categorias/guardanapos.html')

def souplats(request):
    return render(request, 'categorias/souplats.html')

def jogos_americanos(request):
    return render(request, 'categorias/jogos_americanos.html')

def pratos(request):
    return render(request, 'categorias/pratos.html')

def pratos_sobremesa(request):
    return render(request, 'categorias/pratos_sobremesa.html')

def porta_guardanapos(request):
    return render(request, 'categorias/porta_guardanapos.html')

def tacas(request):
    return render(request, 'categorias/tacas.html')

def talheres(request):
    return render(request, 'categorias/talheres.html')

def trilhos_de_mesa(request):
    return render(request, 'categorias/trilhos_de_mesa.html')

def cha_e_cafe_da_tarde(request):
    return render(request, 'categorias/cha_e_cafe_da_tarde.html')

def carrinho(request):
    return render(request, 'categorias/carrinho.html')

def cadastro(request):
    return render(request, 'categorias/cadastro.html')

def login(request):
    return render(request, 'categorias/login.html')

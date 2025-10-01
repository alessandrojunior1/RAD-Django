from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from datetime import date

def hello():
    return HttpResponse("Bem-vindo ao meu blog")

def eco(textoDigitado):
    return HttpResponse(f"Você digitou: {textoDigitado}")

def info():
    return JsonResponse(
        {
            "Disciplina": "RAD",
            "Framework": "Django",
            "Semestre": "2025.2",
        }
    )

def user(request):
    
    contexto = {
        "usuario" : "Alessandro",
        "numero" : 5,
        "flag_is_logged_in" : True,
        "idade" : 18,
        "role" : "admin"

    }
    return render(request, "user.html", contexto)

def products(request):

    produtos = [
        {"nome": "maçã", "preco": 5.00},
        {"nome": "laranja", "preco": 3.00},
        {"nome": "abacaxi", "preco": 7.00},
        {"nome": "pera", "preco": 12.00},
        {"nome": "banana", "preco": 3.00}
    ]

    contexto = {
        "produtos" : produtos
    }

    return render(request, "products.html", contexto)

def home(request):
    return render(request, "home.html")

def contato(request):
    return render(request, "contato.html")

def about(request):
    return render(request, "about.html")
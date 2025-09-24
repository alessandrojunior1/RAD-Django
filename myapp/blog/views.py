from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

def hello(request):
    return HttpResponse("Bem-vindo ao meu blog")

def eco(request,textoDigitado):
    return HttpResponse(f"Você digitou: {textoDigitado}")

def info(request):
    return JsonResponse(
        {
            "Disciplina": "RAD",
            "Framework": "Django",
            "Semestre": "2025.2",
        }
    )
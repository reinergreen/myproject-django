from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def home(request):
    return HttpResponse("acho que deu certo")


def teste(request):
    return HttpResponse("olá,pagina de entrada!")

from django.shortcuts import render
from django.http import HttpResponse


def home(request):
    return render(request, 'receitas/home.html', context={'name': 'Luciano', })


def contato(request):
    return HttpResponse('contato novo 1')


def sobre(request):
    return HttpResponse('sobre novo 1')

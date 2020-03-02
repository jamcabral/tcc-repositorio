from django.shortcuts import render
from django.http import HttpResponse
from .models import Turma, tcc, Defesa


def HomeView(request):
    return render(request, 'index.html')


def TccView(request):
    data = {}
    data['turma'] = Turma.objects.all()
    data['tcc'] = tcc.objects.all()
    data['defesa'] = Defesa.objects.all()
    return render(request, 'tcc.html', data)

def tabelaView(request):
    data = {}
    data['tcc'] = tcc.objects.all()
    data['turma'] = Turma.objects.all()
    data['defesa'] = Defesa.objects.all()
    return render(request, 'tabela.html', data)

def DefesaView(request):
    data = {}
    data['tcc'] = tcc.objects.all()
    data['turma'] = Turma.objects.all()
    data['defesa'] = Defesa.objects.all()
    return render(request, 'defesa.html', data)
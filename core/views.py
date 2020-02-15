from django.shortcuts import render
from django.http import HttpResponse
from .models import Turma


def HomeView(request):
    return render(request, 'index.html')


def TccView(request):
    data = {}
    data['turma'] = Turma.objects.all()
    return render(request, 'tcc.html', data)

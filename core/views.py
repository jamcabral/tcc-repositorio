from django.shortcuts import render
from django.http import HttpResponse


def HomeView(request):
    return render(request, 'index.html')


def TccView(request):
    return render(request, 'tcc.html')

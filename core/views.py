from django.shortcuts import render
from django.http import HttpResponse
from .models import Turma, tcc, Defesa
from datetime import datetime
from django.utils import timezone


def timezone_today():
    """
    Return the current date in the current time zone.
    """
    if settings.USE_TZ:
        return timezone.localtime(timezone.now()).date()
    else:
        return datetime.date.today()

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
    data['time'] = timezone.now()
    return render(request, 'defesa.html', data )

from datetime import datetime

def a_view(request):
    return render_to_response("a_template.html", {
        'time':datetime.now(),
        }, context_instance=RequestContext(request))
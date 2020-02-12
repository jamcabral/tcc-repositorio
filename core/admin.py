from django.contrib import admin
from .models import Curso, Turma, Professor, Coordenador, Aluno, Sala, Tcc, AppTcc

# Register your models here.
admin.site.site_header = "TCC SISTEMA"
admin.site.site_title = "TCC SISTEMA"
admin.site.index_title = "TCC SISTEMA"

admin.site.register(Curso)
admin.site.register(Turma)
admin.site.register(Professor)
admin.site.register(Coordenador)
admin.site.register(Aluno)
admin.site.register(Sala)
admin.site.register(Tcc)
admin.site.register(AppTcc)



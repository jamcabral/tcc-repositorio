from django.contrib import admin
from .models import Curso, Turma, Professor, Coordenador, Aluno, Sala, Tcc, Defesa

# Register your models here.
admin.site.site_header = "TCC SISTEMA"
admin.site.site_title = "TCC SISTEMA"
admin.site.index_title = "TCC SISTEMA"


class CursoAdmin(admin.ModelAdmin):
    list_display = ('id_curso', 'nome_curso')
    search_fields = ['id_curso', 'nome_curso']

class TurmaAdmin(admin.ModelAdmin):
    list_display = ('id_turma', 'nome_turma', 'id_curso_turma', 'periodo_turma')
    search_fields = ['id_turma', 'nome_turma', 'id_curso_turma', 'periodo_turma']
    autocomplete_fields = ['id_curso_turma' ]

class ProfessorAdmin(admin.ModelAdmin):
    list_display = ('id_professor', 'nome_professor', 'matricula_professor', 'condicao_professor')
    search_fields = ['id_professor', 'nome_professor', 'matricula_professor', 'condicao_professor']

class AlunoAdmin(admin.ModelAdmin):
    list_display = ('mat_aluno', 'nome_aluno', 'id_curso_aluno')
    search_fields = ['mat_aluno', 'nome_aluno', 'id_curso_aluno']
    autocomplete_fields = ['id_curso_aluno' ]


class SalaAdmin(admin.ModelAdmin):
    list_display = ('id_sala', 'nome_sala', 'localizacao_sala')
    search_fields = ['id_sala', 'nome_sala', 'localizacao_sala']

class TccAdmin(admin.ModelAdmin):
    list_display = ('id_tcc', 'id_aluno_tcc', 'ano_tcc', 'tema_tcc', 'id_curso_tcc', 'orientador_tcc', 'co_orientador_tcc', 'carta_aceite_tcc', 'convite_banca_tcc', 'marcacao_banca_tcc')
    search_fields = ['id_tcc', 'id_aluno_tcc', 'ano_tcc', 'tema_tcc', 'id_curso_tcc', 'orientador_tcc', 'co_orientador_tcc', 'carta_aceite_tcc', 'convite_banca_tcc', 'marcacao_banca_tcc']
    autocomplete_fields = ['id_aluno_tcc', 'id_curso_tcc', 'orientador_tcc', 'co_orientador_tcc', ]


class DefesaAdmin(admin.ModelAdmin):
    list_display = ('id_tcc_df', 'id_sala_df', 'dt_df', 'banca1_df', 'banca2_df')
    search_fields = ['id_tcc_df', 'id_sala_df', 'dt_df', 'banca1_df', 'banca2_df']
    autocomplete_fields = ['id_sala_df', 'banca1_df', 'banca2_df']


class CoordenadorAdmin(admin.ModelAdmin):
    list_display = ('id_coordenador', 'nome_coordenador', 'id_curso_coordenador')
    search_fields = ['id_coordenador', 'nome_coordenador', 'id_curso_coordenador']
    autocomplete_fields = ['id_curso_coordenador']

admin.site.register(Curso, CursoAdmin)
admin.site.register(Defesa, DefesaAdmin)
admin.site.register(Coordenador, CoordenadorAdmin)
admin.site.register(Turma, TurmaAdmin)
admin.site.register(Professor, ProfessorAdmin)
admin.site.register(Aluno, AlunoAdmin)
admin.site.register(Sala, SalaAdmin)
admin.site.register(Tcc, TccAdmin)
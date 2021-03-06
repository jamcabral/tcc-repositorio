from django.contrib import admin
from admin_auto_filters.filters import AutocompleteFilter
from .models import Curso, Turma, Professor, Coordenador, Aluno, Sala, tcc, Defesa, Periodo

# Register your models here.
admin.site.site_header = "TCC SISTEMA"
admin.site.site_title = "TCC SISTEMA"
admin.site.index_title = "TCC SISTEMA"


class PeriodoAdmin(admin.ModelAdmin):
    list_display = ('nome_periodo', )
    search_fields = ['nome_periodo',]
admin.site.register(Periodo, PeriodoAdmin)

class CursoAdmin(admin.ModelAdmin):
    list_display = ('nome_curso',)
    search_fields = ['nome_curso', ]
    #autocomplete_fields = ['id_periodo_curso' ]
admin.site.register(Curso, CursoAdmin)


class TurmaAdmin(admin.ModelAdmin):
    list_display = ('nome_turma', 'id_curso_turma', 'id_periodo_turma')
    search_fields = ['nome_turma', 'id_curso_turma__nome_curso','id_periodo_turma__nome_periodo' ,]
    autocomplete_fields = ['id_curso_turma', 'id_periodo_turma' ]
admin.site.register(Turma, TurmaAdmin)

class ProfessorAdmin(admin.ModelAdmin):
    list_display = ('nome_professor', 'matricula_professor', 'condicao_professor')
    search_fields = [ 'nome_professor', 'matricula_professor', 'condicao_professor']
    list_display_links = ( 'nome_professor', 'matricula_professor', 'condicao_professor',)
admin.site.register(Professor, ProfessorAdmin)


class AlunoAdmin(admin.ModelAdmin):
    list_display = ('matricula_aluno', 'nome_aluno', 'id_curso_aluno')
    search_fields = ['matricula_aluno', 'nome_aluno', 'id_curso_aluno__nome_curso']
    autocomplete_fields = ['id_curso_aluno' ]
admin.site.register(Aluno, AlunoAdmin)



class SalaAdmin(admin.ModelAdmin):
    list_display = ('nome_sala', 'localizacao_sala')
    search_fields = ['nome_sala', 'localizacao_sala']
admin.site.register(Sala, SalaAdmin)


class tccAdmin(admin.ModelAdmin):
    list_display = ('id_aluno_tcc', 'id_turma_tcc',  'tema_tcc', 'orientador_tcc', 'co_orientador_tcc', 'carta_aceite_tcc', 'convite_banca_tcc', 'marcacao_banca_tcc')
    list_select_related = ['id_turma_tcc']
    search_fields = ['id_aluno_tcc__nome_aluno', 'tema_tcc', 'id_turma_tcc__nome_turma', 'id_turma_tcc__periodo_turma']
    autocomplete_fields = ['id_aluno_tcc', 'id_turma_tcc', 'orientador_tcc', 'co_orientador_tcc', ]
    raw_id_fields = ("professor_disciplica_tcc",)
    list_display_links = ('id_aluno_tcc', 'id_turma_tcc', 'tema_tcc', 'orientador_tcc', 'co_orientador_tcc', 'carta_aceite_tcc', 'convite_banca_tcc', 'marcacao_banca_tcc',)
admin.site.register(tcc, tccAdmin)


class CoordenadorAdmin(admin.ModelAdmin):
    list_display = ('nome_coordenador', 'id_curso_coordenador', 'status_coordenador', 'dt_inicial', 'dt_final',)
    search_fields = ['nome_coordenador', 'id_curso_coordenador__nome_curso', 'status_coordenador', ]
    autocomplete_fields = ['id_curso_coordenador']
admin.site.register(Coordenador, CoordenadorAdmin)



class DefesaAdmin(admin.ModelAdmin):
    list_display = ('dt_df','id_teste', 'id_sala_df', 'banca1_df', 'banca2_df')
    search_fields = ['id_teste__tema_tcc']
    search_fields = ['dt_df']
    autocomplete_fields = ['id_teste', 'id_sala_df', 'banca1_df', 'banca2_df']
admin.site.register(Defesa, DefesaAdmin)

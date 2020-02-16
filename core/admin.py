from django.contrib import admin
from .models import Curso, Turma, Professor, Coordenador, Aluno, Sala, tcc, Defesa

# Register your models here.
admin.site.site_header = "TCC SISTEMA"
admin.site.site_title = "TCC SISTEMA"
admin.site.index_title = "TCC SISTEMA"


class CursoAdmin(admin.ModelAdmin):
    list_display = ('id_curso', 'nome_curso')
    search_fields = ['id_curso', 'nome_curso']
admin.site.register(Curso, CursoAdmin)


class TurmaAdmin(admin.ModelAdmin):
    list_display = ('id_turma', 'nome_turma', 'id_curso_turma', 'periodo_turma')
    search_fields = ['id_turma', 'nome_turma', 'id_curso_turma', 'periodo_turma']
    autocomplete_fields = ['id_curso_turma' ]
admin.site.register(Turma, TurmaAdmin)

class ProfessorAdmin(admin.ModelAdmin):
    list_display = ('id_professor', 'nome_professor', 'matricula_professor', 'condicao_professor')
    search_fields = ['id_professor', 'nome_professor', 'matricula_professor', 'condicao_professor']
admin.site.register(Professor, ProfessorAdmin)


class AlunoAdmin(admin.ModelAdmin):
    list_display = ('mat_aluno', 'nome_aluno', 'id_curso_aluno')
    search_fields = ['mat_aluno', 'nome_aluno', 'id_curso_aluno']
    autocomplete_fields = ['id_curso_aluno' ]
admin.site.register(Aluno, AlunoAdmin)



class SalaAdmin(admin.ModelAdmin):
    list_display = ('id_sala', 'nome_sala', 'localizacao_sala')
    search_fields = ['id_sala', 'nome_sala', 'localizacao_sala']
admin.site.register(Sala, SalaAdmin)


class tccAdmin(admin.ModelAdmin):
    list_display = ('id_tcc', 'id_aluno_tcc', 'id_turma_tcc', 'id_turma_tcc__periodo_turma',  'tema_tcc', 'id_curso_tcc', 'orientador_tcc', 'co_orientador_tcc', 'carta_aceite_tcc', 'convite_banca_tcc', 'marcacao_banca_tcc')
    list_select_related = ['id_turma_tcc']
    search_fields = ['id_turma_tcc__periodo_turma',]
    autocomplete_fields = ['id_aluno_tcc', 'id_turma_tcc', 'id_curso_tcc', 'orientador_tcc', 'co_orientador_tcc', ]
    def id_turma_tcc__periodo_turma(self, obj): # criar um objeto apartir do forenkey do model, e estanciar o atributo dentro de outro model
        return obj.id_turma_tcc.periodo_turma # obj."Atributo do model interno"."atributo do model externo"
    id_turma_tcc__periodo_turma.short_description = 'Turma Periodo'  #Renames column head

admin.site.register(tcc, tccAdmin)

class DefesaAdmin(admin.ModelAdmin):
    list_display = ('id_tcc_df', 'id_sala_df', 'dt_df', 'banca1_df', 'banca2_df')
    search_fields = ['id_tcc_df', 'id_sala_df', 'dt_df', 'banca1_df', 'banca2_df']
    autocomplete_fields = ['id_sala_df', 'banca1_df', 'banca2_df']

admin.site.register(Defesa, DefesaAdmin)


class CoordenadorAdmin(admin.ModelAdmin):
    list_display = ('id_coordenador', 'nome_coordenador', 'id_curso_coordenador')
    search_fields = ['id_coordenador', 'nome_coordenador', 'id_curso_coordenador']
    autocomplete_fields = ['id_curso_coordenador']
admin.site.register(Coordenador, CoordenadorAdmin)



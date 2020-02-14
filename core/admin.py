from django.contrib import admin
from .models import Curso, Turma, Professor, Coordenador, Aluno, Sala, Tcc, Defesa

# Register your models here.
admin.site.site_header = "TCC SISTEMA"
admin.site.site_title = "TCC SISTEMA"
admin.site.index_title = "TCC SISTEMA"

admin.site.register(Turma)
admin.site.register(Professor)
admin.site.register(Coordenador)
admin.site.register(Aluno)
admin.site.register(Sala)
admin.site.register(Tcc)


class CursoAdmin(admin.ModelAdmin):
    list_display = ('id_curso', 'nome_curso')
    search_fields = ['id_curso', 'nome_curso']

"""
class radiologia_examesAdmin(ModelAdmin):
    list_display = ('nome_paciente_paciente', 'radilogia_categoria', 'dt_solicitacao_exame', 'status_radiologia_exame', 'nome_tec_radiologia', 'anexo_radiologia_exame',
     'anexo2_radiologia_exame', 'anexo3_radiologia_exame', 'anexo4_radiologia_exame', 'anexo5_radiologia_exame',)
    search_fields = ['nome_paciente_paciente__nome_paciente', 'nome_paciente_paciente__cpf_paciente', 'status_radiologia_exame','nome_paciente_paciente__dt_nascimento_paciente']
    autocomplete_fields = ['radilogia_categoria', 'nome_paciente_paciente', 'nome_tec_radiologia']
    fieldsets = (
        ('AREA DE SOLICITAÇÃO DE EXAMES (MÉDICOS)', {
            'fields': ('nome_paciente_paciente', 'dt_nascimento_exame', 'radilogia_categoria', 'obs_radiologia_exame')
        }),
        ('AREA PARA EXECUÇÃO DE EXAMES (TEC. RADIOLOGIA)', {
            'classes': ('collapse',),
            'fields': ('anexo_radiologia_exame', 'anexo2_radiologia_exame', 'anexo3_radiologia_exame', 'anexo4_radiologia_exame', 'anexo5_radiologia_exame',
            'status_radiologia_exame', 'nome_tec_radiologia','dt_realizado_exame',),
        }),
    )
    

class radiologia_categoriaAdmin(ModelAdmin):
    search_fields = ['nome_radiologia_categoria']
    list_display = ('nome_radiologia_categoria', 'id_radiologia_categoria',)
"""

class DefesaAdmin(admin.ModelAdmin):
    list_display = ('id_tcc_df', 'id_sala_df', 'dt_df', 'banca1_df', 'banca2_df')
    search_fields = ['id_tcc_df', 'id_sala_df', 'dt_df', 'banca1_df', 'banca2_df']


admin.site.register(Curso, CursoAdmin)
admin.site.register(Defesa, DefesaAdmin)


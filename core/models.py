from django.db import models
from django.conf import settings
from django.contrib.auth.models import User, auth, AbstractBaseUser
from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _


# Create your models here.

def tcc_directory_path(instance, filename):
    return 'uploads/tcc/{0}/{1}'.format(instance.id_tcc, filename)

class Periodo(models.Model):
    id_periodo = models.AutoField(verbose_name="Identificador Periodo", primary_key=True)
    nome_periodo = models.CharField(max_length=6, blank=False, null=False)
    def __str__(self):
        return self.nome_periodo
    class Meta:
        verbose_name = '2 - Periodo'
        verbose_name_plural = '2 - Periodos'


class Curso(models.Model):
    id_curso = models.AutoField(verbose_name="Identificador Curso", primary_key=True)
    nome_curso = models.CharField(verbose_name="Nome do Curso", max_length=50)
    def __str__(self):
        return 'Curso: ' +self.nome_curso 
    class Meta:
        verbose_name = '1 - Curso'
        verbose_name_plural = '1 - Cursos'


class Turma(models.Model):
    class STATUS_TURMA_CHOICE(models.TextChoices):
        ATIVO = 'ATIVO', _('ATIVO'),
        ENCERRADA = 'ENCERRADA', _('ENCERRADA'),

    id_turma = models.AutoField(primary_key=True)
    nome_turma = models.CharField(verbose_name="Nome da Turma", max_length=50)
    id_curso_turma = models.ForeignKey(Curso, verbose_name="Curso", related_name="id_curso_turma", on_delete=models.CASCADE)
    id_periodo_turma = models.ForeignKey (Periodo, related_name='id_periodo_turma', on_delete=models.CASCADE, blank=True, null=True)
    status_turma = models.CharField(verbose_name="Em Andamento ou Encerrada", max_length=50, choices=STATUS_TURMA_CHOICE.choices, default=STATUS_TURMA_CHOICE.ATIVO, blank=True, null=True)
    def __str__(self):
        return 'Turma: ' + self.nome_turma 
        #+ '  |   Periodo: ' + self.id_periodo_turma__nome_periodo
    class Meta:
        verbose_name = '5 - Turma'
        verbose_name_plural = '5 - Turmas'

class Professor(models.Model):
    class CONDICAO_CHOICE(models.TextChoices):
        INTERNO = 'INTERNO', _('INTERNO'),
        EXTERNO = 'EXTERNO', _('EXTERNO'),
    class STATUS_CHOICE(models.TextChoices):
        ATIVO = 'ATIVO', _('ATIVO'),
        INATIVO = 'INATIVO', _('INATIVO'),
    
    id_professor = models.AutoField(verbose_name="Matricula Professor", primary_key=True)
    nome_professor = models.CharField(verbose_name="Nome Professor", max_length=50)
    matricula_professor = models.CharField(verbose_name="Matricula Professor", max_length=50)
    condicao_professor = models.CharField(verbose_name="Externo ou Interno", max_length=50, choices=CONDICAO_CHOICE.choices, default=CONDICAO_CHOICE.INTERNO)
    status_coordenador = models.CharField(verbose_name="Externo ou Interno", max_length=50, choices=STATUS_CHOICE.choices, default=STATUS_CHOICE.ATIVO)
    dt_inicial = models.DateField(verbose_name="Data Inicial")
    dt_final = models.DateField(verbose_name="Data Final", blank=True, null=True)    
    def __str__(self):
        return self.nome_professor
    class Meta:
        verbose_name = '4 - Professor'
        verbose_name_plural = '4 - Professores'

class Coordenador(models.Model):
    class STATUS_CHOICE(models.TextChoices):
        ATIVO = 'ATIVO', _('ATIVO'),
        INATIVO = 'INATIVO', _('INATIVO'),
    
    id_coordenador = models.AutoField(verbose_name="Identificador Coordenador", primary_key=True)
    nome_coordenador = models.CharField(verbose_name="Nome Coordenador", max_length=50)
    matricula_coordenador = models.CharField(verbose_name="Matricula Coordenador", max_length=50)
    id_curso_coordenador = models.ForeignKey(Curso, related_name='id_curso_coordenador', verbose_name="Curso", on_delete=models.CASCADE)
    status_coordenador = models.CharField(verbose_name="Ativo ou Inativo", max_length=50, choices=STATUS_CHOICE.choices, default=STATUS_CHOICE.ATIVO)
    dt_inicial = models.DateField(verbose_name="Data Inicial")
    dt_final = models.DateField(verbose_name="Data Final", blank=True, null=True)
    def __str__(self):
        return self.nome_coordenador
    class Meta:
        verbose_name = '3 - Coordenador'
        verbose_name_plural = '3 - Coordenadores'


class Aluno(models.Model):
    mat_aluno = models.AutoField(verbose_name="Id Aluno", primary_key=True)
    matricula_aluno = models.CharField(verbose_name="Matricula do Aluno", blank=True, null=True)
    nome_aluno = models.CharField(verbose_name="Nome Aluno", max_length=50)
    matricula_aluno = models.CharField(verbose_name="Matricula Aluno", max_length=15)
    id_curso_aluno = models.ForeignKey(Curso, related_name="id_curso_aluno", verbose_name="Curso", on_delete=models.CASCADE)
    def __str__(self):
        return  self.nome_aluno
    class Meta:
        verbose_name = '7 - Aluno'
        verbose_name_plural = '7 - Alunos'

class Sala(models.Model):
    id_sala = models.AutoField(primary_key=True)
    nome_sala = models.CharField(verbose_name="Nome Sala", max_length=50)
    localizacao_sala = models.CharField(verbose_name="Localização da Sala", max_length=50)
    def __str__(self):
        return self.nome_sala
    class Meta:
        verbose_name = '6 - Sala'
        verbose_name_plural = '6 - Salas'


class tcc(models.Model):
    class STATUS_CHOICE(models.TextChoices):
        EmCurso = 'Em Curso', _('Em Curso'),
        abandono = 'Abandono', _('Abandono'),
        reprovado = 'Reprovado', _('Reprovado'),
        aprovado = 'Aprovado', _('Aprovado'),
    
    class STATUS_CD_CHOICE(models.TextChoices):
        Nao = 'Não', _('Não'),
        Sim = 'Sim', _('Sim'),

    id_tcc = models.AutoField(primary_key=True)
    professor_disciplica_tcc = models.ForeignKey(Professor, related_name='professor_disciplica_tcc', on_delete=models.CASCADE)
    id_aluno_tcc = models.ForeignKey(Aluno,verbose_name="Aluno", related_name='id_aluno_tcc', on_delete=models.CASCADE)
    id_turma_tcc = models.ForeignKey(Turma,verbose_name="Turma", on_delete=models.CASCADE)
    tema_tcc = models.CharField(verbose_name="Tema TCC", max_length=100)
    orientador_tcc = models.ForeignKey(Professor, related_name='orientador_tcc', on_delete=models.CASCADE)
    co_orientador_tcc = models.ForeignKey(Professor, related_name='co_orientador_tcc', on_delete=models.CASCADE)
    carta_aceite_tcc = models.FileField(verbose_name="Cartade Aceita", upload_to=tcc_directory_path, blank=True, null=True)
    convite_banca_tcc = models.FileField(verbose_name="Convite Banca", upload_to=tcc_directory_path , blank=True, null=True)
    marcacao_banca_tcc = models.FileField(verbose_name="Marcação Banca", upload_to=tcc_directory_path, blank=True, null=True)
    entrega_cd_tcc = models.CharField(max_length=50, choices=STATUS_CD_CHOICE.choices, default=STATUS_CD_CHOICE.Nao)
    status_tcc = models.CharField(max_length=50, choices=STATUS_CHOICE.choices, default=STATUS_CHOICE.EmCurso)
    def __str__(self):
        return 'Titulo: ' + self.tema_tcc + '  |   Autor: ' + self.id_aluno_tcc.nome_aluno  
    class Meta:
        verbose_name = '8 - Tcc'
        verbose_name_plural = '8 - Tccs'
    

class Defesa(models.Model):
    id_df = models.AutoField(verbose_name="Identificador Apresentacao", primary_key=True)
    id_teste = models.ForeignKey(tcc, on_delete=models.CASCADE, default=None, verbose_name="Tema Apresentação TCC")
    id_sala_df = models.ForeignKey(Sala, related_name='id_sala_df', on_delete=models.CASCADE)
    dt_df = models.DateTimeField()
    banca1_df = models.ForeignKey(Professor, related_name='banca1_df', on_delete=models.CASCADE, blank=True, null=True)
    banca2_df = models.ForeignKey(Professor, related_name='banca2_df', on_delete=models.CASCADE, blank=True, null=True)
    def __str__(self):
        return self.id_sala_df.nome_sala
    class Meta:
        verbose_name = '9 - Defesa'
        verbose_name_plural = '9 - Defesas'
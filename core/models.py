from django.db import models
from django.conf import settings
from django.contrib.auth.models import User, auth, AbstractBaseUser
from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _


# Create your models here.

def tcc_directory_path(instance, filename):
    return 'uploads/tcc/{0}/{1}'.format(instance.id_tcc, filename)

class Curso(models.Model):
    id_curso = models.AutoField(verbose_name="Identificador Curso", primary_key=True)
    nome_curso = models.CharField(verbose_name="Nome do Curso", max_length=50)
    def __str__(self):
        return self.nome_curso
    class Meta:
        verbose_name = 'Curso'
        verbose_name_plural = 'Cursos'


class Turma(models.Model):
    class STATUS_TURMA_CHOICE(models.TextChoices):
        ATIVO = 'ATIVO', _('ATIVO'),
        ENCERRADA = 'ENCERRADA', _('ENCERRADA'),
    id_turma = models.AutoField(primary_key=True)
    nome_turma = models.CharField(verbose_name="Nome da Turma", max_length=50)
    id_curso_turma = models.ForeignKey(Curso, related_name="id_curso_turma", on_delete=models.CASCADE)
    periodo_turma = models.CharField(verbose_name="Periodo Turma", max_length=6)
    status_turma = models.CharField(verbose_name="Em Andamento ou Encerrada", max_length=50, choices=STATUS_TURMA_CHOICE.choices, default=STATUS_TURMA_CHOICE.ATIVO, blank=True, null=True)
    def __str__(self):
        return self.nome_turma
    class Meta:
        verbose_name = 'Turma'
        verbose_name_plural = 'Turmas'

class Professor(models.Model):
    class CONDICAO_CHOICE(models.TextChoices):
        INTERNO = 'INTERNO', _('INTERNO'),
        EXTERNO = 'EXTERNO', _('EXTERNO'),
    
    id_professor = models.AutoField(verbose_name="Matricula Professor", primary_key=True)
    nome_professor = models.CharField(verbose_name="Nome Professor", max_length=50)
    matricula_professor = models.CharField(verbose_name="Matricula Professor", max_length=50)
    condicao_professor = models.CharField(verbose_name="Externo ou Interno", max_length=50, choices=CONDICAO_CHOICE.choices, default=CONDICAO_CHOICE.INTERNO)
    def __str__(self):
        return self.nome_professor
    class Meta:
        verbose_name = 'Professor'
        verbose_name_plural = 'Professores'

class Coordenador(models.Model):
    id_coordenador = models.AutoField(verbose_name="Identificador Coornedaor", primary_key=True)
    nome_coordenador = models.CharField(verbose_name="Nome Coordenador", max_length=50)
    id_curso_coordenador = models.ForeignKey(Curso, related_name="id_curso_coordenador", verbose_name="Curso", on_delete=models.CASCADE)
    def __str__(self):
        return self.nome_coordenador
    class Meta:
        verbose_name = 'Coordenador'
        verbose_name_plural = 'Coordenadores'


class Aluno(models.Model):
    mat_aluno = models.AutoField(verbose_name="Matricula Aluno", primary_key=True)
    nome_aluno = models.CharField(verbose_name="Nome Aluno", max_length=50)
    id_curso_aluno = models.ForeignKey(Curso, related_name="id_curso_aluno", verbose_name="Curso", on_delete=models.CASCADE)
    def __str__(self):
        return  self.nome_aluno
    class Meta:
        verbose_name = 'Aluno'
        verbose_name_plural = 'Alunos'

class Sala(models.Model):
    id_sala = models.AutoField(primary_key=True)
    nome_sala = models.CharField(verbose_name="Nome Sala", max_length=50)
    localizacao_sala = models.CharField(verbose_name="Localização da Sala", max_length=50)
    def __str__(self):
        return self.nome_sala
    class Meta:
        verbose_name = 'Sala'
        verbose_name_plural = 'Salas'


class Tcc(models.Model):
    id_tcc = models.AutoField(verbose_name="Identificador TCC", primary_key=True)
    id_aluno_tcc = models.ForeignKey(Aluno, related_name='id_aluno_tcc', on_delete=models.CASCADE)
    id_turma_tcc = models.ForeignKey(Turma, on_delete=models.CASCADE)
    tema_tcc = models.CharField(verbose_name="Tema TCC", max_length=100)
    id_curso_tcc = models.ForeignKey(Curso, related_name='id_curso_tcc', on_delete=models.CASCADE)
    orientador_tcc = models.ForeignKey(Professor, related_name='orientador_tcc', on_delete=models.CASCADE)
    co_orientador_tcc = models.ForeignKey(Professor, related_name='co_orientador_tcc', on_delete=models.CASCADE)
    carta_aceite_tcc = models.FileField(verbose_name="CartadeAceita", upload_to=tcc_directory_path, blank=True, null=True)
    convite_banca_tcc = models.FileField(verbose_name="ConviteBanca", upload_to=tcc_directory_path , blank=True, null=True)
    marcacao_banca_tcc = models.FileField(verbose_name="MarcaçãoBanca", upload_to=tcc_directory_path, blank=True, null=True)
    def __str__(self):
        return 'TEMA: ' + self.tema_tcc + '  |   Nome: ' + self.id_aluno_tcc.nome_aluno
    class Meta:
        verbose_name = 'Tcc'
        verbose_name_plural = 'Tccs'
    

class Defesa(models.Model):
    id_df = models.AutoField(verbose_name="Identificador Apresentacao", primary_key=True)
    id_tcc_df = models.ForeignKey(Tcc, related_name='id_tcc_df', on_delete=models.CASCADE)
    id_sala_df = models.ForeignKey(Sala, related_name='id_sala_df', on_delete=models.CASCADE)
    dt_df = models.DateTimeField(verbose_name="Data e Hora da Apresentacao", auto_now=False, auto_now_add=False)
    banca1_df = models.ForeignKey(Professor, related_name='banca1_df', on_delete=models.CASCADE, blank=True, null=True)
    banca2_df = models.ForeignKey(Professor, related_name='banca2_df', on_delete=models.CASCADE, blank=True, null=True)
    def __str__(self):
        return self.id_sala_df.nome_sala
    class Meta:
        verbose_name = 'Defesa'
        verbose_name_plural = 'Defesas'
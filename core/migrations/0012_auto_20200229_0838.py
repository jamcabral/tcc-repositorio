# Generated by Django 3.0.3 on 2020-02-29 11:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0011_auto_20200229_0807'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='aluno',
            options={'verbose_name': '7 - Aluno', 'verbose_name_plural': '7 - Alunos'},
        ),
        migrations.AlterModelOptions(
            name='coordenador',
            options={'verbose_name': '3 - Coordenador', 'verbose_name_plural': '3 - Coordenadores'},
        ),
        migrations.AlterModelOptions(
            name='curso',
            options={'verbose_name': '1 - Curso', 'verbose_name_plural': '1 - Cursos'},
        ),
        migrations.AlterModelOptions(
            name='defesa',
            options={'verbose_name': '9 - Defesa', 'verbose_name_plural': '9 - Defesas'},
        ),
        migrations.AlterModelOptions(
            name='periodo',
            options={'verbose_name': '2 - Periodo', 'verbose_name_plural': '2 - Periodos'},
        ),
        migrations.AlterModelOptions(
            name='professor',
            options={'verbose_name': '4 - Professor', 'verbose_name_plural': '4 - Professores'},
        ),
        migrations.AlterModelOptions(
            name='sala',
            options={'verbose_name': '6 - Sala', 'verbose_name_plural': '6 - Salas'},
        ),
        migrations.AlterModelOptions(
            name='tcc',
            options={'verbose_name': '8 - Tcc', 'verbose_name_plural': '8 - Tccs'},
        ),
        migrations.AlterModelOptions(
            name='turma',
            options={'verbose_name': '5 - Turma', 'verbose_name_plural': '5 - Turmas'},
        ),
        migrations.AddField(
            model_name='coordenador',
            name='dt_final',
            field=models.DateField(default='2020-01-01', verbose_name='Data Final'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='coordenador',
            name='dt_inicial',
            field=models.DateField(default='2020-01-01', verbose_name='Data Inicial'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='coordenador',
            name='matricula_coordenador',
            field=models.CharField(default='2020-01-01', max_length=50, verbose_name='Matricula Coordenador'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='coordenador',
            name='status_coordenador',
            field=models.CharField(choices=[('ATIVO', 'ATIVO'), ('INATIVO', 'INATIVO')], default='ATIVO', max_length=50, verbose_name='Externo ou Interno'),
        ),
        migrations.AddField(
            model_name='professor',
            name='dt_final',
            field=models.DateField(default='2020-01-01', verbose_name='Data Final'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='professor',
            name='dt_inicial',
            field=models.DateField(default='2020-01-01', verbose_name='Data Inicial'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='professor',
            name='status_coordenador',
            field=models.CharField(choices=[('ATIVO', 'ATIVO'), ('INATIVO', 'INATIVO')], default='ATIVO', max_length=50, verbose_name='Externo ou Interno'),
        ),
        migrations.AlterField(
            model_name='coordenador',
            name='id_coordenador',
            field=models.AutoField(primary_key=True, serialize=False, verbose_name='Identificador Coordenador'),
        ),
        migrations.AlterField(
            model_name='defesa',
            name='id_tcc_df',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='id_tcc_df', to='core.tcc'),
        ),
        migrations.AlterField(
            model_name='turma',
            name='id_curso_turma',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='id_curso_turma', to='core.Curso', verbose_name='Curso'),
        ),
    ]

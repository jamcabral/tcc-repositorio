# Generated by Django 3.0.3 on 2020-02-15 15:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_auto_20200214_1355'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aluno',
            name='id_curso_aluno',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='id_curso_aluno', to='core.Curso', verbose_name='Curso'),
        ),
        migrations.AlterField(
            model_name='coordenador',
            name='id_curso_coordenador',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='id_curso_coordenador', to='core.Curso', verbose_name='Curso'),
        ),
        migrations.AlterField(
            model_name='defesa',
            name='banca1_df',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='banca1_df', to='core.Professor'),
        ),
        migrations.AlterField(
            model_name='defesa',
            name='banca2_df',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='banca2_df', to='core.Professor'),
        ),
        migrations.AlterField(
            model_name='defesa',
            name='id_sala_df',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='id_sala_df', to='core.Sala'),
        ),
        migrations.AlterField(
            model_name='defesa',
            name='id_tcc_df',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='id_tcc_df', to='core.Tcc'),
        ),
        migrations.AlterField(
            model_name='tcc',
            name='ano_tcc',
            field=models.CharField(max_length=6, verbose_name='Ano'),
        ),
        migrations.AlterField(
            model_name='tcc',
            name='co_orientador_tcc',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='co_orientador_tcc', to='core.Professor'),
        ),
        migrations.AlterField(
            model_name='tcc',
            name='id_aluno_tcc',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='id_aluno_tcc', to='core.Aluno'),
        ),
        migrations.AlterField(
            model_name='tcc',
            name='id_curso_tcc',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='id_curso_tcc', to='core.Curso'),
        ),
        migrations.AlterField(
            model_name='tcc',
            name='orientador_tcc',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='orientador_tcc', to='core.Professor'),
        ),
        migrations.AlterField(
            model_name='turma',
            name='id_curso_turma',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='id_curso_turma', to='core.Curso'),
        ),
    ]
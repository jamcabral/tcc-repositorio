# Generated by Django 3.0.3 on 2020-03-01 13:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0023_auto_20200301_1007'),
    ]

    operations = [
        migrations.AlterField(
            model_name='defesa',
            name='id_tcc_df_df',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='id_tcc_df_df', to='core.tcc'),
        ),
        migrations.CreateModel(
            name='dfe',
            fields=[
                ('id_dfe', models.AutoField(primary_key=True, serialize=False, verbose_name='Identificador Apresentacao')),
                ('dt_dfe', models.DateTimeField(verbose_name='Data e Hora da Apresentacao')),
                ('banca1_dfe', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='banca1_dfe', to='core.Professor')),
                ('banca2_dfe', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='banca2_dfe', to='core.Professor')),
                ('id_sala_dfe', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='id_sala_dfe', to='core.Sala')),
                ('id_tcc_dfe', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='id_tcc_dfe', to='core.tcc')),
            ],
        ),
    ]

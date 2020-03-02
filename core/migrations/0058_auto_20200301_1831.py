# Generated by Django 3.0.3 on 2020-03-01 21:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0057_auto_20200301_1830'),
    ]

    operations = [
        migrations.AddField(
            model_name='curso',
            name='id_periodo_curso',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='id_periodo_curso', to='core.Periodo'),
        ),
        migrations.AlterField(
            model_name='defesa',
            name='id_teste',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='core.tcc', verbose_name='Tema Apresentação TCC'),
        ),
    ]
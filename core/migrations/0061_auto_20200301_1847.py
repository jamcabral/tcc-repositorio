# Generated by Django 3.0.3 on 2020-03-01 21:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0060_auto_20200301_1839'),
    ]

    operations = [
        migrations.AlterField(
            model_name='defesa',
            name='id_teste',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='core.tcc', verbose_name='Tema Apresentação TCC'),
        ),
    ]

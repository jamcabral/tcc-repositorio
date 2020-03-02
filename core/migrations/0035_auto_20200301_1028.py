# Generated by Django 3.0.3 on 2020-03-01 13:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0034_auto_20200301_1028'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dfe',
            name='id_tcc_dfe',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='id_tcc_dfe', to='core.tcc'),
        ),
        migrations.AlterField(
            model_name='periodo',
            name='id_tcc_periodo',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='id_tcc_periodo', to='core.tcc'),
        ),
    ]

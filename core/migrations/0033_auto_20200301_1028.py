# Generated by Django 3.0.3 on 2020-03-01 13:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0032_auto_20200301_1027'),
    ]

    operations = [
        migrations.AddField(
            model_name='periodo',
            name='id_tcc_periodo',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='id_tcc_periodo', to='core.tcc'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='dfe',
            name='id_tcc_dfe',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='id_tcc_dfe', to='core.tcc'),
        ),
    ]

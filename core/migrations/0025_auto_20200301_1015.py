# Generated by Django 3.0.3 on 2020-03-01 13:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0024_auto_20200301_1015'),
    ]

    operations = [
        migrations.AlterField(
            model_name='defesa',
            name='id_tcc_df_df',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='id_tcc_df_df', to='core.tcc'),
        ),
        migrations.AlterField(
            model_name='dfe',
            name='id_tcc_dfe',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='id_tcc_dfe', to='core.tcc'),
        ),
    ]

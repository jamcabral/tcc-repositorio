# Generated by Django 3.0.3 on 2020-03-01 14:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0039_auto_20200301_1132'),
    ]

    operations = [
        migrations.AddField(
            model_name='dfe',
            name='id_tccajuste_dfe',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='id_tccajuste_dfe', to='core.TccAjuste'),
            preserve_default=False,
        ),
    ]

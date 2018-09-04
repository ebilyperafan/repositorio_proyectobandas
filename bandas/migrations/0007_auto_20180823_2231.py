# Generated by Django 2.0.6 on 2018-08-24 03:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bandas', '0006_auto_20180823_1821'),
    ]

    operations = [
        migrations.AlterField(
            model_name='banda',
            name='nacionalidad',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bandas.Nacionalidad'),
        ),
        migrations.AlterField(
            model_name='integrante',
            name='banda',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bandas.Banda'),
        ),
    ]

# Generated by Django 2.0.6 on 2018-08-14 22:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bandas', '0002_auto_20180814_1639'),
    ]

    operations = [
        migrations.RenameField(
            model_name='banda',
            old_name='foto',
            new_name='photo',
        ),
    ]

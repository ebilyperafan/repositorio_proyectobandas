# Generated by Django 2.0.6 on 2018-08-14 21:39

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('bandas', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Perfil',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('foto', models.ImageField(blank=True, null=True, upload_to='perfiles')),
                ('identificacion', models.CharField(max_length=100)),
                ('edad', models.CharField(max_length=100)),
                ('user', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='banda',
            name='foto',
            field=models.ImageField(blank=True, null=True, upload_to='fotos'),
        ),
        migrations.AddField(
            model_name='integrante',
            name='foto',
            field=models.ImageField(blank=True, null=True, upload_to='fotos'),
        ),
    ]

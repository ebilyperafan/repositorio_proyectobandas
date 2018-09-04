# Generated by Django 2.0.6 on 2018-07-31 21:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Banda',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_banda', models.CharField(max_length=100)),
                ('numero_integrantes', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Integrante',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('edad', models.IntegerField()),
                ('nombre', models.CharField(max_length=100)),
                ('genero', models.CharField(choices=[('MS', 'Masculino'), ('FM', 'Femenino')], default='MS', max_length=2)),
                ('direccion', models.TextField(max_length=30)),
                ('banda', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='bandas.Banda')),
            ],
        ),
        migrations.CreateModel(
            name='Nacionalidad',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_nacionalidad', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Rol',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_rol', models.CharField(max_length=100)),
            ],
        ),
        migrations.AddField(
            model_name='integrante',
            name='roles',
            field=models.ManyToManyField(blank=True, null=True, to='bandas.Rol'),
        ),
        migrations.AddField(
            model_name='banda',
            name='nacionalidad',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='bandas.Nacionalidad'),
        ),
    ]

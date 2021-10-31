# Generated by Django 3.2.6 on 2021-10-30 21:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Equipo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(default='', max_length=200)),
                ('imagen', models.CharField(default='', max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(default='', max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Integrante',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('UsuarioEquipo', models.CharField(default='', max_length=200)),
                ('fecha', models.DateField(verbose_name='Fecha de Ingreso')),
                ('equipo', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='nielsapp.equipo')),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='nielsapp.usuario')),
            ],
        ),
    ]

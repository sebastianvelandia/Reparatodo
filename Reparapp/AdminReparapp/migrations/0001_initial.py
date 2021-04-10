# Generated by Django 3.1.7 on 2021-04-09 21:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('TecnicoReparapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('username', models.CharField(max_length=50, unique=True, verbose_name='Nombre de usuario')),
                ('email', models.EmailField(max_length=254, unique=True, verbose_name='Correo electrónico')),
                ('nombres', models.CharField(blank=True, max_length=50, null=True, verbose_name='Nombres')),
                ('apellidos', models.CharField(blank=True, max_length=50, null=True, verbose_name='Apellidos')),
                ('usuario_activo', models.BooleanField(default=True)),
                ('usuario_administrador', models.BooleanField(default=True)),
                ('usuario_agente', models.BooleanField(default=False)),
                ('usuario_tecnico', models.BooleanField(default=False)),
                ('usuario_operador', models.BooleanField(default=False)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Agente',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='AdminReparapp.usuario')),
                ('agente_id', models.CharField(max_length=50, unique=True)),
                ('telefono', models.CharField(max_length=20)),
            ],
            options={
                'verbose_name': 'Agente',
                'verbose_name_plural': 'Agentes',
            },
        ),
        migrations.CreateModel(
            name='TecnicoEspecialista',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='AdminReparapp.usuario')),
                ('tecnico_id', models.CharField(max_length=50, unique=True)),
                ('telefono', models.CharField(max_length=20)),
                ('taller', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='TecnicoReparapp.taller')),
            ],
            options={
                'verbose_name': 'TecnicoEspecialista',
                'verbose_name_plural': 'TecnicosEspecialistas',
            },
        ),
        migrations.CreateModel(
            name='Operador',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='AdminReparapp.usuario')),
                ('operador_id', models.CharField(max_length=50, unique=True)),
                ('telefono', models.CharField(max_length=20)),
                ('call_center', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='TecnicoReparapp.callcenter')),
            ],
            options={
                'verbose_name': 'Operador',
                'verbose_name_plural': 'Operadores',
            },
        ),
    ]

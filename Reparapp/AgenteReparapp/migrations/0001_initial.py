# Generated by Django 3.2 on 2021-04-12 19:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('AdminReparapp', '0001_initial'),
        ('TecnicoReparapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('cliente_id', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=50)),
                ('telefono', models.CharField(max_length=10)),
            ],
            options={
                'verbose_name': 'Cliente',
                'verbose_name_plural': 'Clientes',
            },
        ),
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('codigo_id', models.AutoField(primary_key=True, serialize=False)),
                ('averia', models.TextField()),
                ('nombre_electrodomestico', models.CharField(max_length=50)),
            ],
            options={
                'verbose_name': 'Producto',
                'verbose_name_plural': 'Productos',
            },
        ),
        migrations.CreateModel(
            name='Orden',
            fields=[
                ('orden_id', models.AutoField(primary_key=True, serialize=False)),
                ('observaciones', models.TextField()),
                ('estado', models.CharField(choices=[('RE', 'Reparado'), ('RC', 'Recepcionado'), ('ER', 'En Reparación'), ('IN', 'Informada'), ('CE', 'Cerrada')], default='RC', max_length=2)),
                ('fecha_ingreso', models.DateField(auto_now_add=True)),
                ('agente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='AdminReparapp.agente')),
                ('cliente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='AgenteReparapp.cliente')),
                ('producto', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='AgenteReparapp.producto')),
                ('tecnico_epecialista', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='AdminReparapp.tecnicoespecialista')),
            ],
            options={
                'verbose_name': 'Orden',
                'verbose_name_plural': 'Ordenes',
            },
        ),
        migrations.CreateModel(
            name='Factura',
            fields=[
                ('factura_id', models.AutoField(primary_key=True, serialize=False)),
                ('costo_orden', models.IntegerField()),
                ('fecha_retiro', models.DateField()),
                ('agente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='AdminReparapp.agente')),
                ('callCenter', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='TecnicoReparapp.callcenter')),
                ('orden', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='AgenteReparapp.orden')),
            ],
            options={
                'verbose_name': 'Factura',
                'verbose_name_plural': 'Facturas',
            },
        ),
    ]

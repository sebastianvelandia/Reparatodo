<<<<<<< HEAD
# Generated by Django 3.1.7 on 2021-04-10 21:02
=======
# Generated by Django 3.1.7 on 2021-04-06 03:14
>>>>>>> parent of c9a8782... login

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CallCenter',
            fields=[
                ('callCenter_NIT', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('nombre_callcenter', models.CharField(max_length=50)),
                ('direccion', models.CharField(max_length=50)),
            ],
            options={
                'verbose_name': 'CallCenter',
                'verbose_name_plural': 'CallCenters',
            },
        ),
        migrations.CreateModel(
            name='Taller',
            fields=[
                ('taller_id', models.AutoField(primary_key=True, serialize=False)),
                ('nombre_taller', models.CharField(max_length=50)),
            ],
            options={
                'verbose_name': 'Taller',
                'verbose_name_plural': 'Talleres',
            },
        ),
    ]

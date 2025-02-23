# Generated by Django 5.1.3 on 2024-12-15 21:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='VehiculoModelo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('marca', models.CharField(choices=[('FIAT', 'Fiat'), ('CHEVROLET', 'Chevrolet'), ('FORD', 'Ford'), ('TOYOTA', 'Toyota')], default='FORD', max_length=20)),
                ('modelo', models.CharField(max_length=100)),
                ('serial_carroceria', models.CharField(max_length=50)),
                ('serial_motor', models.CharField(max_length=50)),
                ('categoria', models.CharField(choices=[('PARTICULAR', 'Particular'), ('TRANSPORTE', 'Transporte'), ('CARGA', 'Carga')], default='PARTICULAR', max_length=20)),
                ('precio', models.FloatField()),
                ('fecha_creacion', models.DateTimeField(auto_now_add=True)),
                ('fecha_modificacion', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]

# Generated by Django 5.1.3 on 2024-12-16 18:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vehiculo', '0002_alter_vehiculomodelo_options'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='VehiculoModelo',
            new_name='VehiculoModel',
        ),
    ]

# Generated by Django 5.1.3 on 2024-12-16 04:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vehiculo', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='vehiculomodelo',
            options={'permissions': (('visualizar_catalogo', 'Visualizar catálogo de Vehículos'),)},
        ),
    ]

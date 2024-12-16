from django.db import models

class VehiculoModel(models.Model):
    marcas_choices = (
        ('FIAT', 'Fiat'),
        ('CHEVROLET', 'Chevrolet'),
        ('FORD', 'Ford'),
        ('TOYOTA', 'Toyota'),
    )
    categoria_choices = (
        ('PARTICULAR', 'Particular'),
        ('TRANSPORTE', 'Transporte'),
        ('CARGA', 'Carga'),
    )
    marca = models.CharField(max_length=20, choices=marcas_choices, default='FORD')
    modelo = models.CharField(max_length=100)
    serial_carroceria = models.CharField(max_length=50)
    serial_motor = models.CharField(max_length=50)
    categoria = models.CharField(max_length=20, choices=categoria_choices, default='PARTICULAR')
    precio = models.FloatField()
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_modificacion = models.DateTimeField(auto_now=True)

    class Meta:
        permissions = (
            ('visualizar_catalogo', 'Visualizar catálogo de Vehículos'),
        )

    def __str__(self):
        return self.modelo
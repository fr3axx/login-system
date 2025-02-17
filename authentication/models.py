from django.db import models
from django.contrib.auth.models import User

class Producto(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.PositiveIntegerField()
    imagen = models.ImageField(upload_to='static/img/', null=True, blank=True)

    def __str__(self):
        return self.nombre
    
class Moneda(models.Model):
    MONEDA_CHOICES = [
        ('bolivares', 'Bolivares'),
        ('dolares', 'Dolares'),
    ]

    tipo_moneda = models.CharField(max_length=26, choices=MONEDA_CHOICES )

    def __str__(self):
        return self.tipo_moneda
    
class TipodePago(models.Model):
    tipo_pago = models.CharField(max_length=50, default='none')
    moneda = models.ForeignKey(Moneda, on_delete=models.CASCADE)

    def __str__(self):
        return self.tipo_pago

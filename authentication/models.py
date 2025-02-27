from django.db import models
from django.contrib.auth.models import User

class Producto(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.PositiveIntegerField()
<<<<<<< Updated upstream
    imagen = models.ImageField(upload_to='productos/', null=True, blank=True)
=======
    imagen = models.ImageField(upload_to='media/static/img', null=True, blank=True)
>>>>>>> Stashed changes

    def __str__(self):
        return self.nombre

class Carrito(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    productos = models.ManyToManyField(Producto, through='CarritoProducto')
    subtotal = models.DecimalField(max_digits=10, decimal_places=2, default=0.0)
    total = models.DecimalField(max_digits=10, decimal_places=2, default=0.0)

    def calcular_totales(self):
        self.subtotal = sum(producto.precio for producto in self.productos.all())
        self.total = self.subtotal  # Puedes agregar más lógica para calcular el total si es necesario

    def save(self, *args, **kwargs):
        self.calcular_totales()  # Calcula los totales antes de guardar
        super().save(*args, **kwargs)  # Guarda el objeto

class CarritoProducto(models.Model):
    carrito = models.ForeignKey(Carrito, on_delete=models.CASCADE)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cantidad = models.PositiveIntegerField(default=1)

class Moneda(models.Model):
    MONEDA_CHOICES = [
        ('bolivares', 'Bolivares'),
        ('dolares', 'Dolares'),
    ]

    tipo_moneda = models.CharField(max_length=26, choices=MONEDA_CHOICES)

    def __str__(self):
        return self.tipo_moneda

class TipodePago(models.Model):
    tipo_pago = models.CharField(max_length=50, default='none')
    moneda = models.ForeignKey(Moneda, on_delete=models.CASCADE)

    def __str__(self):
        return self.tipo_pago
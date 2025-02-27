from django.db import models
from django.contrib.auth.models import User

class Producto(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.PositiveIntegerField()
    imagen = models.ImageField(upload_to='productos/', null=True, blank=True)

    def __str__(self):
        return self.nombre

class Carrito(models.Model):
    usuario = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return f"Carrito de {self.usuario.username}"

    def agregar_producto(self, producto):
        carrito_producto, created = CarritoProducto.objects.get_or_create(carrito=self, producto=producto)
        if not created:
            carrito_producto.cantidad += 1
            carrito_producto.save()

    def eliminar_producto(self, producto):
        carrito_producto = CarritoProducto.objects.get(carrito=self, producto=producto)
        if carrito_producto.cantidad > 1:
            carrito_producto.cantidad -= 1
            carrito_producto.save()
        else:
            carrito_producto.delete()

    def vaciar_carrito(self):
        self.carritoproducto_set.all().delete()

class CarritoProducto(models.Model):
    carrito = models.ForeignKey(Carrito, on_delete=models.CASCADE)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cantidad = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f"{self.cantidad} x {self.producto.nombre} en el carrito de {self.carrito.usuario.username}"

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


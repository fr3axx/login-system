from django.contrib import admin
from .models import TipodePago, Moneda, Producto

# Register your models here.
admin.site.register(Producto)
admin.site.register(TipodePago)
admin.site.register(Moneda)

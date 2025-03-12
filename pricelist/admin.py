from django.contrib import admin

# Register your models here.

from .models import Proveedor,Factura,DetalleFactura

admin.site.register(Proveedor)
admin.site.register(Factura)
admin.site.register(DetalleFactura)
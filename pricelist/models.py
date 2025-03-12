from django.db import models

# Create your models here.
from django.conf import settings
from django.utils import timezone
from django.core.validators import MinLengthValidator

class Proveedor(models.Model):
    IDProveedor = models.AutoField(primary_key=True)
    razonSocial = models.CharField(max_length=200)
    cuit = models.CharField('CUIT',max_length=11,validators=[MinLengthValidator(11)])
    domicilio = models.CharField(max_length=200)
    telefono = models.CharField(max_length=20)
    email = models.EmailField()
    web = models.URLField()

    def __str__(self):
        return f"{self.razonSocial} {self.cuit}"
    

class Factura(models.Model):
    IDFactura = models.AutoField(primary_key=True)
    IDProveedor= models.ForeignKey(Proveedor, on_delete=models.CASCADE)
    FechaFactura = models.DateField()
    PuntoVenta = models.IntegerField()
    NumFactura = models.IntegerField()
    Dolar1 = models.FloatField()
    Dolar2 = models.FloatField()

    def __str__(self):
        return f"{self.FechaFactura} {self.PuntoVenta}-{self.NumFactura}"


class DetalleFactura(models.Model):
    # codigoProveedor= models.CharField(max_length=200)
    IDDetalleFactura = models.AutoField(primary_key=True)
    IDFactura = models.ForeignKey(Factura, on_delete=models.CASCADE)
    codigoInterno= models.CharField(max_length=200)
    descripcion= models.TextField()
    tasaiva = models.FloatField()
    # moneda = models.CharField(max_length=5)
    pesoscompra= models.FloatField()
    # dolar1= models.FloatField()
    # dolar2= models.FloatField()
    dolarescompra= models.FloatField()
    ubicacion = models.CharField(max_length=200)
    coef = models.FloatField()




import datetime
from django.db import models

class DateTimeModel(models.Model):
     created_at=models.DateTimeField(default=datetime.datetime.now())
     updated_at=models.DateTimeField(default=datetime.datetime.now())
     deleted_at= models.DateTimeField(null= True, blank = True)


     class Meta:
          abstract=True

            
class Cliente(DateTimeModel):
    name = models.CharField(max_length=20)
    lastname=models.CharField(max_length=20)
    email=models.EmailField(null= True, blank = True)
    phone= models.CharField(null= True, blank = True)

    def _str_(self):
         return f"{self.email}-{self.password}"

class Productos( DateTimeModel):
     nombre = models.CharField(max_length=20)
     abreviatura = models.CharField(max_length=20)
     descripcion = models.CharField(max_length=20)

class ClienteProducto(DateTimeModel):
    id_cliente = models.IntegerField()
    id_producto = models.IntegerField()
    numero_cuenta = models.CharField(max_length=100)

class TipoTransacciones(DateTimeModel):
    nombre = models.CharField(max_length=100)
    abreviatura = models.CharField(max_length=50)
    descripcion = models.TextField()         


class Transaction(DateTimeModel):
    id_cliente_producto = models.IntegerField()
    monto = models.DecimalField(max_digits=10, decimal_places=2)
    tipo_transaccion = models.CharField(max_length=50)




# Create your models here.

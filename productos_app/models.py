from django.db import models

# Create your models here.
class Producto(models.Model):
    id_producto=models.PositiveSmallIntegerField(primary_key=True)
    nombre=models.CharField(max_length=10)
    tamaño=models.FloatField((""))
    precio=models.FloatField((""))
    calidad=models.CharField(max_length=10)
    cantidad=models.PositiveSmallIntegerField()
    peso=models.FloatField((""))
    def __str__(self) -> str:
        return self.nombre


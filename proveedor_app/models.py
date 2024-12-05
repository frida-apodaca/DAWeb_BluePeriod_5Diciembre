from django.db import models

# Create your models here.
class Proveedor(models.Model):
    id_proveedor=models.PositiveSmallIntegerField(primary_key=True)
    nombre=models.CharField(max_length=10)
    productos=models.CharField(max_length=20)
    cantidad_productos=models.FloatField((""))
    direccion=models.CharField(max_length=10)
    fecha_contratacion=models.DateField(null=False,blank=False)
    sueldo=models.FloatField((""))
    def __str__(self) -> str:
        return self.nombre

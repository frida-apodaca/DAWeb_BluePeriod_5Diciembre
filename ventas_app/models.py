from django.db import models

# Create your models here.
class Ventas(models.Model):
    id_venta=models.PositiveSmallIntegerField(primary_key=True)
    id_empleado=models.PositiveSmallIntegerField()
    id_cliente=models.PositiveSmallIntegerField()
    fecha_venta=models.DateField(null=False,blank=False)
    cantidad=models.FloatField((""))
    total=models.FloatField((""))
    def __str__(self) -> str:
        return self.id_empleado

from django.db import models

# Create your models here.
class Empleado(models.Model):
    id_empleado=models.PositiveSmallIntegerField(primary_key=True)
    nombre=models.CharField(max_length=10)
    fecha_nacimiento=models.DateField(null=False,blank=False)
    sueldo=models.FloatField((""))
    sexo=models.CharField(max_length=10)
    telefono=models.PositiveSmallIntegerField()
    direccion=models.CharField(max_length=10)
    fecha_ingreso=models.DateField(null=False,blank=False)
    
    def __str__(self) -> str:
        return self.nombre

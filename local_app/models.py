from django.db import models

# Create your models here.
class Local(models.Model):
    id_Local=models.PositiveSmallIntegerField(primary_key=True)
    nombre=models.CharField(max_length=10)
    capacidad=models.CharField(max_length=10)
    empleados=models.CharField(max_length=10)
    dueño=models.CharField(max_length=10)
    direccion=models.CharField(max_length=10)
    telefono=models.PositiveSmallIntegerField()
    def __str__(self) -> str:
        return self.nombre

from django.db import models

# Create your models here.
class Cliente(models.Model):
    id_cliente=models.PositiveSmallIntegerField(primary_key=True)
    nombre=models.CharField(max_length=10)
    sexo=models.CharField(max_length=10)
    productos=models.CharField(max_length=10)
    historial=models.CharField(max_length=10)
    metodo_pago=models.CharField(max_length=10)
    telefono=models.PositiveSmallIntegerField()
    def __str__(self) -> str:
        return self.nombre


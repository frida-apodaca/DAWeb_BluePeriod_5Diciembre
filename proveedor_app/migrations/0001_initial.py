# Generated by Django 5.1.4 on 2024-12-05 05:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Proveedor',
            fields=[
                ('id_proveedor', models.PositiveSmallIntegerField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=10)),
                ('productos', models.CharField(max_length=20)),
                ('cantidad_productos', models.FloatField(verbose_name='')),
                ('direccion', models.CharField(max_length=10)),
                ('fecha_contratacion', models.DateField()),
                ('sueldo', models.FloatField(verbose_name='')),
            ],
        ),
    ]
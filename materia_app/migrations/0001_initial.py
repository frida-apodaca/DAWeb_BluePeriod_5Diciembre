# Generated by Django 5.1.4 on 2024-12-05 05:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Materia',
            fields=[
                ('codigo', models.CharField(max_length=6, primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=100)),
                ('creditos', models.PositiveSmallIntegerField()),
            ],
        ),
    ]
from django.db import models


# Create your models here.
class User(models.Model):
    nombre = models.CharField(max_length=30)
    direccion = models.CharField(max_length=30)
    email = models.EmailField()
    telefono = models.CharField(max_length=30)


class Projects(models.Model):
    nombre = models.CharField(max_length=30)
    descripcion = models.CharField(max_length=30)
    estado = models.CharField(max_length=10)


class Productos(models.Model):
    nombre = models.CharField(max_length=30)
    descripcion = models.CharField(max_length=30)
    cantidad = models.IntegerField()

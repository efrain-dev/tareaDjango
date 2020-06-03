from django.db import models


# Create your models here.
class Trabajador(models.Model):
    nombre = models.CharField(max_length=30)
    direccion = models.CharField(max_length=30)
    email = models.EmailField()
    telefono = models.CharField(max_length=30)
    dpi = models.CharField(max_length=30)

    def __str__(self):
        return '%s' % self.nombre


class Cliente(models.Model):
    nombre = models.CharField(max_length=30)
    direccion = models.CharField(max_length=30)
    email = models.EmailField()
    telefono = models.CharField(max_length=30)

    def __str__(self):
        return '%s' % self.nombre


class Project(models.Model):
    nombre = models.CharField(max_length=30)
    descripcion = models.CharField(max_length=250)
    estado = models.CharField(max_length=15)

    def __str__(self):
        return '%s' % self.nombre


class Marca(models.Model):
    nombre = models.CharField(max_length=30)
    descripcion = models.CharField(max_length=30)

    def __str__(self):
        return '%s' % self.nombre


class Producto(models.Model):
    nombre = models.CharField(max_length=30)
    descripcion = models.CharField(max_length=30)
    cantidad = models.IntegerField()
    precio = models.FloatField(default=0)
    marca = models.ForeignKey(Marca, on_delete=models.CASCADE)

    def __str__(self):
        return '%s Stock %s' % (self.nombre, self.cantidad)

from django.db import models
from django.contrib.auth.models import User


class Alumno(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, default='')
    codigo_postal = models.CharField(max_length=10)
    codigo_pais = models.TextField(max_length=2)

    def __str__(self):
        return self.usuario.email


class Curso(models.Model):
    nombre = models.CharField(max_length=100, primary_key=True)
    descripcion = models.TextField(max_length=500)
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField()
    cocinero = models.ForeignKey(User, default='')
    alumnos = models.ManyToManyField(Alumno, default='', blank=True)

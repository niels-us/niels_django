from enum import unique
from django.db import models


class Equipo(models.Model):
    nombre = models.CharField(max_length=200, unique=True, default='')
    imagen = models.ImageField(blank=True, null=True, default='', upload_to='img/')

    def __str__(self):
        return self.nombre


class Usuario(models.Model):
    nombre = models.CharField(max_length=200, unique=True, default='')

    def __str__(self):
        return self.nombre


class Integrante(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    equipo = models.ForeignKey(Equipo, on_delete=models.CASCADE)
    UsuarioEquipo = models.CharField(max_length=200, unique=True, default='')
    fecha = models.DateField('Fecha de Ingreso')

    def __str__(self):
        return self.UsuarioEquipo

from django.db import models


class Equipo(models.Model):
    nombre = models.CharField(max_length=200, default='')
    # imagen = models.CharField(max_length=100, default='')
    imagen = models.ImageField(blank=True, null=True)
    # my_binary_data = models.BinaryField()

    def __str__(self):
        return self.nombre


class Usuario(models.Model):
    nombre = models.CharField(max_length=200, default='')

    def __str__(self):
        return self.nombre


class Integrante(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.RESTRICT)
    equipo = models.ForeignKey(Equipo, on_delete=models.RESTRICT)
    UsuarioEquipo = models.CharField(max_length=200, unique=True, default='')
    fecha = models.DateField('Fecha de Ingreso')

    def __str__(self):
        return self.UsuarioEquipo

from django.db import models

opciones = [
    ('NO','NO'),
    ('SI','SI')
]

class Alumnos(models.Model):
    nombre = models.CharField(max_length=100, verbose_name="Nombre Completo")
    carrera = models.CharField(max_length=100, verbose_name="Carrera")
    grado = models.CharField(max_length=100, verbose_name="Grado | Grupo")
    beca = models.CharField(max_length=100, verbose_name="Beca", choices=opciones)
    

    def __str__(self):
        return self.nombre

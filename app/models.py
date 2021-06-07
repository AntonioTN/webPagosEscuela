# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=200, 
        verbose_name="Nombre")
    lastName = models.CharField(max_length=200, 
        verbose_name="Apellido")
    carrera = models.CharField(max_length=200, 
        verbose_name="Carrera")
    grado = models.CharField(max_length=200, 
        verbose_name="Grado")
    grupo = models.CharField(max_length=200, 
        verbose_name="Grupo")
    created = models.DateTimeField(auto_now_add=True, 
        verbose_name="Fecha de creación")
    updated = models.DateTimeField(auto_now=True,
        verbose_name="Fecha de edición")

    class Meta:
        verbose_name = "Alumno"
        verbose_name_plural = "Alumnos"
        ordering = ["-created"]

    def __str__(self):
        return self.title

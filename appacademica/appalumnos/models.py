from django.db import models

# Create your models here.
class alumno(models.Model):
    codigo = models.CharField(max_length=10)
    nombre = models.CharField(max_length=65)
    direccion = models.CharField(max_length=100)
    telefono = models.CharField(max_length=9)
    
from django.db import models

class materia(models.Model):
    codigo = models.CharField(max_length=2)
    nombre = models.CharField(max_length=65)
    uv = models.SmallIntegerField()

    
class docente(models.Model):
   codigo = models.CharField(max_length=10)
   nombre = models.CharField(max_length=65)
   direccion = models.CharField(max_length=100)
   telefono = models.CharField(max_length=9)
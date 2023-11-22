from django.db import models

# Create your models here.
class Pelicula(models.Model):
    titulo = models.CharField(max_length=30)
    director = models.CharField(max_length=30)
    genero = models.CharField(max_length=30)
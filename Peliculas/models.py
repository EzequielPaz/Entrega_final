from django.db import models
#Importacion para el avatar
from django.contrib.auth.models import User

# Create your models here.
class Pelicula(models.Model):
    titulo = models.CharField(max_length=30)
    director = models.CharField(max_length=30)
    genero = models.CharField(max_length=30)

    def __str__(self):
        return f"Titulo: {self.titulo} - director {self.director} - genero {self.genero}"

class Avatar(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to='avatares', null=True, blank = True)
    descripcion = models.TextField(null=True)
    link = models.URLField(null=True)
    
    def __str__(self):
        return f"{self.user} - {self.imagen}"
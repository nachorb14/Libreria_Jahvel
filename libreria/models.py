from django.db import models

# Create your models here.
class Autor(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    nacionalidad = models.CharField(max_length=50)
    fecha_nacimiento = models.DateField()
    
    def __str__(self):
        return f"{self.nombre} {self.apellido} ({self.nacionalidad})"
    
class Libro(models.Model):
    titulo = models.CharField(max_length=200)
    autor = models.ForeignKey(Autor, on_delete=models.CASCADE)
    fecha_publicacion = models.DateField()
    genero = models.CharField(max_length=50)
    
    def __str__(self):
        return f"{self.titulo} por {self.autor.nombre} {self.autor.apellido}"
    
class Genero(models.Model):
    nombre = models.CharField(max_length=50)
    
    def __str__(self):
        return self.nombre
    
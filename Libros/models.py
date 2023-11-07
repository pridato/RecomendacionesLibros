from django.db import models

# Create your models here.


class Libro(models.Model):
    titulo = models.CharField(max_length=50)
    autor = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=50)
    fecha_publicacion = models.DateField()

    def __str__(self):
        return self.titulo
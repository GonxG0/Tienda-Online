from django.db import models
from django.urls import reverse


class Servicio(models.Model):

    titulo = models.CharField(max_length=50)
    contenido = models.CharField(max_length=50)
    imagen = models.ImageField( upload_to='servicio')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name= "servicio"
        verbose_name_plural= "servicios"


    def __str__(self):
        return self.titulo
    
    
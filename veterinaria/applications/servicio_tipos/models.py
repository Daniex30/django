from django.db import models
from django.db.models.fields import IntegerField

# Create your models here.
class Servicio_tipo(models.Model):
    name = models.CharField('Nombre', max_length= 100,unique=True)

    def __str__(self):
        return str(self.id) + '-' + self.name 
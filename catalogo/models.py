import uuid
from django.db import models 
# Create your models here.

class Juego(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    nombre = models.CharField( max_length=150)
    plataforma = models.CharField(max_length=50)
    precio = models.DecimalField(max_digits=5, decimal_places=2)
    imagen = models.CharField(max_length=200, blank=True, null=True)
    descripcion = models.TextField(blank=True, null=True)
    
    def __str__(self) -> str:
        return f"{self.nombre} ({self.plataforma})"
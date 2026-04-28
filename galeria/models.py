from django.db import models
from django.contrib.auth.models import User

class Foto(models.Model):
    # Vinculamos cada foto a un usuario específico
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    titulo = models.CharField(max_length=100)
    # Las fotos se guardarán físicamente en media/fotos_galeria/
    imagen = models.ImageField(upload_to='fotos_galeria/')
    fecha_subida = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.titulo
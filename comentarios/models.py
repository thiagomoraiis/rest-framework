from django.db import models
from django.contrib.auth.models import User

class Comentarios(models.Model):
    titulo = models.CharField(max_length=100)
    conteudo = models.TextField()
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    data = models.DateTimeField(auto_now_add=True)
    aprovado = models.BooleanField(default=True)

    def __str__(self):
        return self.usuario.username.capitalize()
from django.db import models
from atracoes.models import Atracoes
from comentarios.models import Comentarios
from avaliacoes.models import Avaliacoes
from enderecos.models import Enderecos

class PontosTuristicos(models.Model):
    nome = models.CharField(max_length=50)
    descricao = models.TextField()
    aprovado = models.BooleanField(default=False)
    atracoes = models.ManyToManyField(Atracoes)
    comentario =  models.ManyToManyField(Comentarios)
    avalicao =  models.ManyToManyField(Avaliacoes)
    endereco = models.ForeignKey(Enderecos, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.nome
    

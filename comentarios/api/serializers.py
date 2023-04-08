from rest_framework import serializers
from ..models import Comentarios

class ComentariosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comentarios
        fields = ('titulo', 'conteudo', 'data', 'aprovado')
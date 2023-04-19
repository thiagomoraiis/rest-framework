from rest_framework import serializers
from ..models import Avaliacoes

class AvaliacoesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Avaliacoes
        fields = ('user', 'comentario', 'nota', 'data')
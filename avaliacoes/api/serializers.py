from rest_framework import serializers
from ..models import Avaliacoes

class AvaliacoesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Avaliacoes
        fields = ('comentario', 'nota', 'data')
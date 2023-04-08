from rest_framework import serializers
from ..models import Atracoes

class AtracoesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Atracoes
        fields = ('nome', 'descricao', 'horario_func', 'idade_minima')
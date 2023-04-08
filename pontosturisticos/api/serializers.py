from rest_framework import serializers
from ..models import PontosTuristicos

class PontoTuristicoSerializer(serializers.ModelSerializer):
    class Meta:
        model = PontosTuristicos
        fields = ('id', 'nome', 'descricao')
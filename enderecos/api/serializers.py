from rest_framework import serializers
from ..models import Enderecos

class EnderecoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Enderecos
        fields = ('linha1', 'linha2', 'cidade', 'estado') 
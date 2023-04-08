from rest_framework import viewsets
# from ..api import AtracoesSerializer
from .serializers import AtracoesSerializer
from ..models import Atracoes

class AtracoesViewSet(viewsets.ModelViewSet):
    queryset = Atracoes.objects.all()
    serializer_class = AtracoesSerializer
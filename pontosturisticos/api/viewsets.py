from rest_framework import viewsets
from .serializers import PontoTuristicoSerializer
from ..models import PontosTuristicos

class PontoTuristicoViewSet(viewsets.ModelViewSet):
    queryset = PontosTuristicos.objects.all()
    serializer_class = PontoTuristicoSerializer
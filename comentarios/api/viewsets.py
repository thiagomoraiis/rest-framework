from rest_framework import viewsets
from ..models import Comentarios
from .serializers import ComentariosSerializer

class ComentarioViewSet(viewsets.ModelViewSet):
    queryset = Comentarios.objects.all()
    serializer_class = ComentariosSerializer
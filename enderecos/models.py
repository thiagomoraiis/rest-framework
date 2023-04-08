from django.db import models

class Enderecos(models.Model):
    linha1 = models.CharField(max_length=100)
    linha2 = models.CharField(max_length=100)
    cidade = models.CharField(max_length=100)
    estado = models.CharField(max_length=50)
    latitude = models.IntegerField(blank=True, null=True)
    longitude = models.IntegerField(blank=True, null=True)

    def __str__(self) -> str:
        return f'{self.cidade} {self.estado}'
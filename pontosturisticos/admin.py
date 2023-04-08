from django.contrib import admin
from .models import PontosTuristicos

@admin.register(PontosTuristicos)
class PontosTuristicosAdmin(admin.ModelAdmin):
    list_display = ('nome', 'descricao','aprovado')
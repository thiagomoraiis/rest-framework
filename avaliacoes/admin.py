from django.contrib import admin
from .models import Avaliacoes

@admin.register(Avaliacoes)
class AvaliacoesAdmin(admin.ModelAdmin):
    list_display = ('nota', 'user', 'data')
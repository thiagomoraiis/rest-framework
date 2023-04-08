from django.contrib import admin

from .models import Atracoes

@admin.register(Atracoes)
class AtracoesAdmin(admin.ModelAdmin):
    list_display = ('nome', 'descricao', 'idade_minima', )
from django.contrib import admin
from .models import Comentarios

@admin.register(Comentarios)
class ComentariosAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'usuario', 'data')
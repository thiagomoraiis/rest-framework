from django.contrib import admin
from .models import Enderecos

@admin.register(Enderecos)
class EnderecoAdmin(admin.ModelAdmin):
    list_display = ('cidade', 'estado')
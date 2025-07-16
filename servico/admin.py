from django.contrib import admin
from .models import Servico

@admin.register(Servico)
class ProdutoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'preco')  # campos mostrados na lista do admin
    search_fields = ('nome',)   
from django.contrib import admin
from .models import Produto


class ListandoProdutos(admin.ModelAdmin):
    list_display = ("id", "nome", "preco")
    list_display_links = ("id", "nome")
    search_fields = ("nome",)
    list_filter = ("categoria",)
    list_per_page = 10

admin.site.register(Produto, ListandoProdutos)


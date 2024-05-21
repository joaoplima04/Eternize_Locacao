from django.contrib import admin
from categorias.models import Cliente


class ListandoClientes(admin.ModelAdmin):
    list_display = ("cpf", "nome", "telefone")
    list_display_links = ("cpf", "nome")
    search_fields = ("nome", "cpf")
    list_per_page = 10

admin.site.register(Cliente, ListandoClientes)

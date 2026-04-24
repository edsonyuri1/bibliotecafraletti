from django.contrib import admin
from .models import Autor, Livro, Emprestimo

@admin.register(Autor)
class AutorAdmin(admin.ModelAdmin):
    list_display = ('nome', 'naturalidade') # Colunas que aparecem na lista de autores
    search_fields = ('nome',) # Barra de pesquisa por nome

@admin.register(Livro)
class LivroAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'autor', 'status', 'e_digital') # Colunas da lista de livros
    list_filter = ('status', 'e_digital', 'autor') # Filtros na lateral direita
    search_fields = ('titulo', 'isbn') # Barra de pesquisa

# REGISTRO DO EMPRÉSTIMO
@admin.register(Emprestimo)
class EmprestimoAdmin(admin.ModelAdmin):
    # Colunas que ajudam a controlar quem está com qual livro e quando deve devolver
    list_display = ('livro', 'usuario', 'data_emprestimo', 'data_devolucao')
    list_filter = ('data_emprestimo', 'data_devolucao')
    search_fields = ('livro__titulo', 'usuario__username') # Busca pelo nome do livro ou de quem emprestou


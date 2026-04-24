from django.db import models
from django.contrib.auth.models import User  # Importa o sistema de usuários do Django


# MODELO DE AUTOR
class Autor(models.Model):
    nome = models.CharField(max_length=200, verbose_name="Nome do Autor")
    naturalidade = models.CharField(max_length=100, blank=True, help_text="Ex: Pereiras-SP")

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name_plural = "Autores"


# MODELO DE LIVRO
class Livro(models.Model):
    #  status
    STATUS_CHOICES = [
        ('disponivel', 'Disponível'),
        ('emprestado', 'Emprestado'),
    ]

    titulo = models.CharField(max_length=255, verbose_name="Título do Livro")
    # ForeignKey liga o livro a um Autor. Se o autor for deletado, os livros dele também serão (CASCADE)
    autor = models.ForeignKey(Autor, on_delete=models.CASCADE, related_name="livros")
    ano_publicacao = models.IntegerField(null=True, blank=True)
    isbn = models.CharField(max_length=13, blank=True, verbose_name="ISBN/Registro")

    # Estante Virtual (Campos para livros digitais)
    e_digital = models.BooleanField(default=False, verbose_name="O livro possui versão digital?")
    arquivo_pdf = models.FileField(upload_to='livros_digitais/', blank=True, null=True)

    # Controle do Acervo Físico
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='disponivel')
    localizacao = models.CharField(max_length=100, blank=True, help_text="Ex: Estante A, Prateleira 2")

    def __str__(self):
        return self.titulo


# MODELO DE EMPRÉSTIMO
class Emprestimo(models.Model):
    # Liga o empréstimo a um livro específico
    livro = models.ForeignKey(Livro, on_delete=models.CASCADE)
    # Liga o empréstimo ao usuário que pegou o livro
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Leitor")
    # Define a data do empréstimo automaticamente ao criar
    data_emprestimo = models.DateField(auto_now_add=True)
    # Campo para data de devolução, pode ser vazio até o livro voltar
    data_devolucao = models.DateField(null=True, blank=True)

    def __str__(self):
        return f"{self.livro.titulo} - {self.usuario.username}"

    class Meta:
        verbose_name = "Empréstimo"
        verbose_name_plural = "Empréstimos"

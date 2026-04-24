from django.shortcuts import render
from django.contrib.auth.decorators import login_required # para pedir login antes de entrar no site
from .models import Livro

@login_required(login_url='/admin/login/') # obriga ter login para ver a pagina
def home(request):
    livros = Livro.objects.all()
    return render(request, 'acervo/index.html', {'livros': livros})


# É a função que o Django vai chamar quando alguém acessar o site
def lista_livros(request):
    #  Busca todos os objetos 'Livro' que estão salvos no banco de dados
    # O .all() é o comando que diz: "traga tudo o que encontrar na tabela"
    livros = Livro.objects.all()

    # O comando render combina o  arquivo HTML com os dados buscados
    # 'request' é o pedido do usuário
    # 'acervo/index.html' é o desenho da página
    # {'livros': livros} é a lista que o HTML vai usar para preencher a tela
    return render(request, 'acervo/index.html', {'livros': livros})
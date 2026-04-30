# Projeto Integrador

Este documento foi feito com o intuito de ser um pequeno guia de consulta para a estrutura, tecnologias e comandos 
utilizados no desenvolvimento do projeto.

**Frameworks e Tecnologias utilizadas**

**Python:** Linguagem base do projeto.

**Django:** Framework web, fornece banco de dados, autenticação e admin prontos.

**SQLite:** Banco de dados padrão (posteriormente será alterado para o MySql).

**Jazzmin:** Extensão para o Django Admin que fornece uma opções mais bonitas e personalizáveis.

**Bootstrap Icons:** Biblioteca de ícones via CDN que foi usada na home.

# Passo a Passo do que foi feito:

Para iniciar o projeto foi necessário criar o ambiente virtual e iniciar o Django.

No interpretador de comandos/terminal (também chamado de bash) foram usados os seguintes comandos:

**python -m venv .venv**   <- Comando que cria o ambiente virtual

**.venv\Scripts\activate** <- Ativa o ambiente (Windows)

**pip install django django-jazzmin** <- Instala as bibliotecas (django e jazzmin)

**django-admin startproject ProjetoPiTeste** . <- Cria o projeto e o nome dele.

**python manage.py startapp acervo** <- Cria o app do sistema de acervo

# Definição dos Dados (models.py):
No arquivo acervo/models.py, são definidos as tabelas do banco de dados (Livro, Autor, Emprestimo). 

Para lteramos este arquivo, usamos:

Bash:

**python manage.py makemigrations** <- Prepara a alteração

**python manage.py migrate** <- Aplica a alteração no banco

# Criar usuário:
Bash:

python manage.py createsuperuser <- Cria login/senha para o /admin

# Onde Alterar? 

Interface Administrativa (settings.py)
Para mudar o visual do painel, logos, cores ou botões do menu:

JAZZMIN_SETTINGS <- Altera títulos, logos, ordem do menu e ícones.

JAZZMIN_UI_TWEAKS <- Altera o tema visual (ex: flatly), cores da barra (navbar-purple) e estilo dos botões.

changeform_format: "horizontal_tabs": Remove a barra lateral direita das telas de cadastro.

# Botões do Admin (admin.py)

Para alterar o que aparece quando clicamos em "Livros" ou "Autores" dentro da aba de  Admin editamos o que está em **acervo/admin.py**:

list_display -> Define quais colunas aparecem na lista.

search_fields -> Define onde a barra de busca vai procurar.

fields -> Define quais campos aparecem em "Adicionar". 

# Página Inicial do Usuário (templates/acervo/index.html)

Para fazer alterações dos botões Home:
href="/admin/acervo/livro/add/": Link direto para cadastrar algo.

href="/admin/acervo/livro/": Link para ver a lista de cadastrados.

{% static '...' %}: Caminho para imagens e CSS da pasta static.

# Estilização (static/acervo/css/style.css)

Para mudar cores, fontes, tamanhos de botões ou esconder elementos.

# Para que serve cada coisa:

**manage.py** -> Comandos de terminal (rodar servidor, migrar banco).

**settings.py** ->Configurações globais (Jazzmin, Banco de Dados, Apps instalados).

**urls.py**-> As rotas do site (ex: o que acontece quando digito /admin).

**models.py**-> Estrutura do banco de dados (o que o sistema armazena).

**admin.py**-> Customiza a tela de gestão.

**views.py** -> A "lógica" (pega os livros do banco e manda para o HTML).

**Jazzmin** -> Embeleza o painel administrativo nativo do Django.

# Onde alterar os botões de MODIFICAR E ADICIONAR na aba gestão:

O que aparece na tabela principal -> list_display = ('titulo', 'autor', 'e_digital')

Adicionar barra de pesquisa -> search_fields = ('titulo',) 
    
Filtros da lateral direita -> list_filter = ('autor', 'e_digital')

# O que fazer para alterar do sqlite para MySql
Será necessário instalar o "driver" que permite ao Python conversar com o MySQL:

Bash: **pip install mysqlclient**

**Alteração no settings.py**

Devemos substituir a parte de DATABASES que temos por:

Python


 `DATABASES = {
    
'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'nome_do_seu_banco',
        'USER': 'seu_usuario',
        'PASSWORD': 'sua_password',
        'HOST': 'localhost',   # Ou o IP do servidor onde o MySQL está/ficará
        'PORT': '3306',        # Porta padrão do MySQL
    }`
}

**Migração de Dados**

Quando trocarmos o banco, o MySQL estará vazio. Temos duas opções (como não temos muitos dados cadastrados no nossobanco de dados, talvez seja melhor começar do zero):

**Começar do zero**: Apenas rodar python manage.py migrate no novo banco e cadastrar tudo novamente.

**Migrar os dados:** Usar os comandos  **python manage.py dumpdata** (para exportar do SQLite) e **python manage.py loaddata** (para importar no MySQL).


# Como rodar o projeto:

1 - Clonar o repositório:

bash

**git clone [https://github.com/edsonyuri1/bibliotecafraletti.git](https://github.com/edsonyurii/bibliotecafraletti.git)
cd bibliotecafraletti**

2 - Criar um ambiente virtual 

Bash

**python -m venv .venv**

3 - Ativar o ambiente virtual

Windows: **.venv\Scripts\activate*

4 - Instalar as dependências

Bash

**pip install -r requirements.txt**

5 - Configurar o Banco de Dados

Bash

**python manage.py migrate**

6 - Agora é necessario criar um usuário administrador, ele irá pedir pra um nome de usuario, e-mail (que pode ser deixado em branco) e depois uma senha (ela não aparece ao digitar, é normal). 

Bash

**python manage.py createsuperuser**


7. Iniciar o servidor

Bash

**python manage.py runserver**

Vai gerar um link parecido com esse, é só clicar que ira abrir o app -> http://127.0.0.1:8000

Ele pedirá para entrar com uma conta e senha para acessar o aplicativo, é só colocar o login e senha que você criou.



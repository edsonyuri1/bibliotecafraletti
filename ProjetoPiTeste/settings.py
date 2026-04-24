from pathlib import Path
import os

# Define o caminho base do projeto (onde está o db.sqlite3 e a pasta manage.py)
BASE_DIR = Path(__file__).resolve().parent.parent

# Chave de segurança para criptografia do Django (manter em segredo)
SECRET_KEY = 'django-insecure-0ic_$jsjf28l++*o1o$zs#_xlk97z$n2c!ygk!j7n#rt%1vv@2'

# Se o debug estiver em True, mostrará erros detalhados na tela. Se False, oculta.
DEBUG = True

# Domínios ou IPs que podem acessar o site (vazio permite qualquer um em desenvolvimento)
ALLOWED_HOSTS = []

# --- APLICATIVOS INSTALADOS ---
INSTALLED_APPS = [
    'jazzmin',  # Permite editar o painel administrativo
    'django.contrib.admin',  # Interface  nativa do painel de adm
    'django.contrib.auth',  # Sistema de autenticação (usuários/senhas)
    'django.contrib.contenttypes',  # Permite ao Django rastrear todos os modelos do projeto
    'django.contrib.sessions',  # Gerencia sessões (ex: manter usuário logado)
    'django.contrib.messages',  # Sistema de notificações/alertas
    'django.contrib.staticfiles',  # Gerencia arquivos como CSS, JS e Imagens
    'acervo',  # O aplicativo em si, onde estão os livros e autores
]

# Camadas de segurança e processamento que rodam entre o servidor e o navegador
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',  # Proteção contra ataques em formulários
    'django.contrib.auth.middleware.AuthenticationMiddleware',  # Importante para saber quem está logado
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# Indica qual arquivo controla as rotas/URLs do site
ROOT_URLCONF = 'ProjetoPiTeste.urls'

# Configurações do motor de renderização das páginas HTML
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],  # Pastas extras onde o Django buscaria HTMLs
        'APP_DIRS': True,  # Faz o Django procurar a pasta /templates/ dentro do  app 'acervo'
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

# Configuração para o servidor Web se comunicar com o Django
WSGI_APPLICATION = 'ProjetoPiTeste.wsgi.application'

# Configuração do Banco de Dados (usando SQLite, posteriormente será alterado para mySql da Amanda)
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# Regras de validação de senha (ex: não pode ser muito curta ou comum)
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

# INTERNACIONALIZAÇÃO
LANGUAGE_CODE = 'pt-br'  # Define o idioma do painel admin para Português Brasil
TIME_ZONE = 'America/Sao_Paulo'  # Define o fuso horário para o Brasil
USE_I18N = True  # Ativa a tradução internacional
USE_TZ = True  # Ativa o uso de fuso horários

# ARQUIVOS ESTÁTICOS (CSS, JS, IMAGENS DO SISTEMA) ---
STATIC_URL = 'static/'
STATICFILES_DIRS = [
    BASE_DIR / 'acervo' / 'static',  # Pasta onde foi guardado o style.css e pereiras.png
]

#  ARQUIVOS DE MÍDIA (PDFS E UPLOADS) ---
MEDIA_URL = '/media/'  # URL para acessar arquivos enviados (ex: capas de livros)
MEDIA_ROOT = BASE_DIR / 'media'  # Pasta física onde os PDFs salvos ficarão

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

#  REDIRECIONAMENTOS DE LOGIN
LOGIN_REDIRECT_URL = '/'  # Para onde o usuário vai após logar (Home)
LOGOUT_REDIRECT_URL = '/admin/login/'  # Para onde vai após sair (Tela de Login do Admin)
SESSION_EXPIRE_AT_BROWSER_CLOSE = True  # True desloga o usuário se ele fechar o navegador

# CONFIGURAÇÕES VISUAIS DO JAZZMIN (ADMIN)
JAZZMIN_SETTINGS = {
    "site_title": "Biblioteca Pereiras",  # Título da aba no navegador
    "site_header": "Pereiras",  # Título no topo do painel
    "site_brand": "Biblioteca Pereiras",  # Nome da marca na barra superior
    "site_logo": "acervo/pereiras.png",  # Logo que aparece no canto superior
    "login_logo": "acervo/pereiras.png",  # Logo que aparece na tela de login
    "welcome_sign": "Bem-vindo(a) à Biblioteca",  # Frase da tela de login
    "copyright": "Biblioteca Municipal Pedro Fraletti",  # Texto do rodapé
    "user_avatar": None,  # Se houver campo de foto de usuário será aqui

    "show_topmenu": True,  # Mostra/Esconde a barra de menu superior
    "show_ui_builder": False,  # Esconde a engrenagem de teste de cores
    "site_url": "/",  # Link para onde a logo da marca leva (Home)

    "topmenu_links": [  # Links rápidos no topo do Admin
        {"name": "Voltar", "url": "home", "permissions": ["auth.view_user"]},
    ],

    "show_sidebar": False,  # False oculta a barra lateral cinza da esquerda no admin
    "navigation_expanded": True,  # Se a barra existisse, ela começaria aberta
    "hide_models": ["auth.group"],  # Esconde a tabela "Grupos"
    "changeform_format": "horizontal_tabs",  # Transforma formulários longos em abas

    # Define a ordem que as tabelas aparecem no dashboard
    "order_with_respect_to": ["acervo.livro", "acervo.emprestimo", "acervo.autor", "auth.user"],

    # Ícones das tabelas (usa nomes da biblioteca Font Awesome)
    "icons": {
        "auth": "fas fa-users",
        "auth.user": "fas fa-user-plus",
        "acervo.livro": "fas fa-book",
        "acervo.autor": "fas fa-pen-nib",
        "acervo.emprestimo": "fas fa-handshake",
    },
    "custom_css": "acervo/css/style.css",  # Caminho do CSS personalizado para o Admin
}

# AJUSTES DE CORES E TEMA DO JAZZMIN
JAZZMIN_UI_TWEAKS = {
    "brand_colour": "navbar-purple",  # Cor da marca na lateral
    "navbar": "navbar-purple navbar-dark",  # Cor da barra superior e estilo do texto
    "navbar_fixed": True,  # Mantém a barra do topo parada ao rolar a página
    "layout_boxed": False,  # Se True, o site fica centralizado com bordas nas laterais
    "theme": "flatly",  # Nome do tema visual escolhido, no caso é o Bootstrap
    "button_classes": {  # Estilo dos botões de ação
        "primary": "btn-primary",
        "secondary": "btn-secondary",
        "info": "btn-info",
        "warning": "btn-warning",
        "danger": "btn-danger",
        "success": "btn-success"
    }
}
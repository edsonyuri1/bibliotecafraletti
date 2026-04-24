from django.contrib import admin
from django.urls import path, include
from acervo import views  # importa as funções que foi salvo no views.py

# Customização do título
admin.site.site_header = "Biblioteca Pereirense"
admin.site.site_title = "Admin Pereiras"
admin.site.index_title = "Gestão do Acervo"

#aqui é o caminho que manda de volta pra home
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
]
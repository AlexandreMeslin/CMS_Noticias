from django.urls import path
from . import views

# Registro do APP
app_name = 'noticias'

# Lista de URLs desse APP
urlpatterns = [
    path('', views.home, name='home-noticias'),
    path('<int:idNoticia>', views.noticiaCompleta, name='noticiaCompleta'),
]

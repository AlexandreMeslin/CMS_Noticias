from django.urls import path
from . import views

app_name = 'anuncios'

urlpatterns = [
    path('', views.home, name='home-anuncios'),
]

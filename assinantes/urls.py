from django.urls import path
from . import views

app_name = 'assinantes'

urlpatterns = [
    path('', views.home, name='home-assinantes'),
]

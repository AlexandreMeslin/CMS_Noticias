from django.shortcuts import render
from django.shortcuts import get_object_or_404  # obter dados do bd
from .models import Noticia    # classe Noticia

def home(request):
    #noticias = Noticia.objects.all()
    #noticias = Noticia.objects.order_by('-data')[:10]
    noticias = Noticia.objects.order_by('-data')
    # 'noticias' --> chave do dicionário
    # noticias --> valor do dicionário
    return render(request, 'noticias/home.html', {'noticias': noticias})

def noticiaCompleta(request, idNoticia):
    noticia = get_object_or_404(Noticia, pk=idNoticia)
    return render(request, 'noticias/noticiaCompleta.html', {'noticia': noticia})

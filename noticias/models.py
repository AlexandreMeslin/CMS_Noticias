from django.db import models

class Noticia(models.Model):
    titulo = models.CharField(max_length=100)
    subtitulo = models.CharField(max_length=200)
    data = models.DateField()
    link = models.URLField(blank=True)
    conteudo = models.TextField()
    imagem = models.ImageField(upload_to='noticias/imagens', blank=True)

    # A pagina admin usa para representar a entrada para o registro
    def __str__(self):
        return self.titulo

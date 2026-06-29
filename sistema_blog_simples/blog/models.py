from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.urls import reverse

class Postagem(models.Model):
    titulo = models.CharField(max_length=200)
    autor = models.ForeignKey(User, on_delete=models.CASCADE)
    conteudo = models.TextField()
    data_postagem = models.DateTimeField(default=timezone.now) 
    
    class Meta:
        verbose_name = 'Postagen'
        
    def __str__(self):
        return self.titulo

    def get_absolute_url(self):
        return reverse('blog-detail', kwargs={'pk': self.pk})
    
class Comentario(models.Model):
    postagem = models.ForeignKey(Postagem, on_delete=models.CASCADE, related_name='comentarios')
    autor = models.ForeignKey(User, on_delete=models.CASCADE)
    texto = models.TextField()
    data_criacao = models.DateTimeField(default=timezone.now)

    class Meta:
        ordering = ['-data_criacao']

    def __str__(self):
        return f'Comentário de {self.autor.username} em {self.postagem.titulo}'
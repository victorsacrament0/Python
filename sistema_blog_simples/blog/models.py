from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class Postagem(models.Model):
    titulo = models.CharField(max_length=200)
    autor = models.ForeignKey(User, on_delete=models.CASCADE)
    conteudo = models.TextField()
    data_postagem = models.DateTimeField(default=timezone.now) 
    
    class Meta:
        verbose_name = 'Postagen'
        
    def __str__(self):
        return self.titulo


from django.db import models

# Create your models here.

class Cliente(models.Model):
    nome = models.CharField(max_length=255)
    cpf = models.CharField(max_length=15, unique=True)
    telefone = models.CharField(max_length=20)

    def __str__(self):
        return self.nome
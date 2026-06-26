from django.db import models

# Create your models here.

class Aluno(models.Model):
    nome = models.CharField(max_length=255)
    curso = models.CharField(max_length=255)
    turma = models.CharField(max_length=255)

    def __str__(self):
        return self.nome

class Campus(models.Model):
    nome = models.CharField(max_length=255, unique=True)

    #Relação com a tabela clientes
    aluno  = models.ForeignKey(Aluno, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Campu'

    def __str__(self):
        return self.nome   
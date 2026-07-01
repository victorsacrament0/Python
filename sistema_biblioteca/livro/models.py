from django.db import models
from datetime import date
from usuario.models import Usuario

class Categoria(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField()
    usuario = models.ForeignKey(Usuario, on_delete=models.DO_NOTHING)
    
    def __str__(self):
        return self.nome


class Livros(models.Model):
    nome = models.CharField(max_length=200)
    autor = models.CharField(max_length=100)
    co_autor = models.CharField(max_length=100, blank=True , null= True)
    data_cadastro = models.DateField(default=date.today)
    emprestado = models.BooleanField(default=False)
    categoria = models.ForeignKey(Categoria, on_delete=models.DO_NOTHING)
    usuario = models.ForeignKey(Usuario, on_delete=models.DO_NOTHING)

    class Meta:
        verbose_name = 'Livro'

    def __str__(self):
        return self.nome


class Emprestimo(models.Model):
    nome_emprestado = models.ForeignKey(Usuario, on_delete=models.CASCADE, blank=True, null= True)
    data_emprestimo = models.DateField(blank=True, null= True)
    data_devolucao = models.DateField(blank=True, null= True)
    livro = models.ForeignKey(Livros, on_delete=models.DO_NOTHING)

    def __str__(self):
        return f'{self.nome_emprestado} | {self.livro}'
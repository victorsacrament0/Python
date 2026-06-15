from django.db import models

class Cliente(models.Model):
    nome = models.CharField(max_length=55)
    sobrenome = models.CharField(max_length=60)
    email = models.EmailField(max_length=150)
    cpf = models.CharField(max_length=15, unique=True)

    def __str__(self):
        return self.nome
    
class Carro(models.Model):
    carro = models.CharField(max_length=255)
    placa = models.CharField(max_length=10)
    ano = models.IntegerField() 
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    lavagens = models.IntegerField(default=0)
    consertos = models.IntegerField(default=0)

    def __str__(self):
        return self.carro
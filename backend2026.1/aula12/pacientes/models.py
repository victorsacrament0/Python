from django.db import models

class Pacientes(models.Model):
    queixa_choices = (
        ('TDAH' , 'Transtorno do Déficit de Atenção com Hiperatividade'),
        ('D' , 'Depressão'),
        ('A' , 'Ansiedade'),
        ('TAG' , 'Transtorno de Ansiedade Generalizada')
    )
    
    nome = models.CharField(max_length=255)
    email = models.EmailField()
    telefone = models.CharField(max_length=255, null=True, blank=True)
    foto = models.ImageField(upload_to='fotos')
    pagamento_em_dia = models.BooleanField(default=True)
    queixa = models.CharField(max_length=255, choices=queixa_choices)

    def __str__(self):
        return self.nome
from django.shortcuts import render
from django.contrib import messages
from .models import Cliente,Conta, Movimento
import random

def index(request):
    return render(request, 'pages/home.html')

def abrir_conta(request):
    if request.method == 'POST':
        nome_form = request.POST.get('nome') 
        cpf_form =  request.POST.get('cpf')

        cpf_limpo = cpf_form.replace('.','').replace('-','').replace('','')
        
        if Cliente.objects.filter(cpf=cpf_limpo).exists():
            messages.error (request, 'Erro! CPF já cadastrado em nosso banco de dados.')
            return render(request, 'pages/abrir_conta.html')
        try:
            cliente = Cliente.objects.create(nome=nome_form,cpf=cpf_limpo)
            numero = str(random.randint(10000, 99999))

            while Conta.objects.filter(numero=numero).exists():
                numero = str(random.randint(10000, 99999))

            conta = Conta.objects.create(numero=numero,cliente=cliente)
        except:
            return

    return render(request, 'pages/abrir_conta.html')




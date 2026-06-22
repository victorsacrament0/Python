from django.shortcuts import render,get_object_or_404,redirect
from django.contrib import messages
from django.db import IntegrityError
from .models import Cliente,Conta, Movimento
from decimal import Decimal
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

            messages.success(request,f'Conta criada com sucesso! Seu número de conta é {numero}')

            return redirect('conta',conta_id=conta.id)

        except IntegrityError:
            messages.error(request, 'Erro ao criar conta, CPF já cadastrado')
            return render(request, 'pages/abrir_conta.html')
        except Exception as e:
            messages.error(request, f'Erro ao criar conta! Erro: {str(e)}')
            return render(request, 'pages/abrir_conta.html')

    return render(request, 'pages/abrir_conta.html')


def conta(request,conta_id):
    
    conta = get_object_or_404(Conta,id=conta_id)
    return render(request,'pages/conta.html',{'conta':conta})

def depositar(request,conta_id):

    conta = get_object_or_404(Conta,id=conta_id)
    if request.method == 'POST':
        try:
            valor = Decimal(request.POST.get('valor_form'))
            if valor > 0:
                conta.depositar(valor)
            
                Movimento.objects.create(conta=conta,tipo='deposito', valor=valor)
                messages.success(request, f'Depósito de R${valor:.2f} realizado!')

                return redirect('conta',conta_id=conta.id)
            else:
                messages.error(request, 'Valor Inválido')
    
        except:
            messages.error(request, 'Valor Inválido')
            
    return render(request, 'pages/depositar.html',{'conta':conta})

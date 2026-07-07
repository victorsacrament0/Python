
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages 
from django.db import IntegrityError
from decimal import Decimal
from django.http import HttpResponse
from .models import Cliente, Conta, Movimento
import random
 

 

def index(request):
    return render(request, 'pages/home.html')
 

def abrir_conta(request):
    
    if request.method == "POST":
        nome_form = request.POST.get('nome')
        cpf_form = request.POST.get('cpf') 

        cpf_limpo = cpf_form.replace('.', '').replace('-', '').replace(' ','')
 
        if Cliente.objects.filter(cpf=cpf_limpo).exists():
            
            messages.error(request, 'CPF já cadastrado! Use outro CPF ou acesse uma conta exixtente.')
            return render(request, 'pages/abrir_conta.html')
       
        try:
            cliente = Cliente.objects.create(nome=nome_form, cpf=cpf_limpo)

            numero = (random.randint(10000, 99999))
  
            while Conta.objects.filter(numero=numero).exists():
                 numero = str(random.randint(10000, 99999))
           
            conta = Conta.objects.create(numero=numero, cliente=cliente)
           
            messages.success(request, f'Conta criada com sucesso! Seu numero de conta é: {numero}')
           
            request.session['conta_numero'] = numero
            
            return redirect('conta', conta_id=conta.id)
       
        
        except IntegrityError:  
            messages.error(request, 'Erro ao criar conta. CPF já cadastrado')
            return render(request, 'pages/abrir_conta.html')
       
        except Exception as e: 
            messages.error(request, f'Erro ao cria a conta: {str(e)}')
            return render(request, 'pages/abrir_conta.html')
   
 
    return render(request, 'pages/abrir_conta.html')
 

def conta(request, conta_id):
    
    conta = get_object_or_404(Conta, id=conta_id)
 
    if 'conta_numero' not in request.session or request.session['conta_numero'] != conta.numero:
        messages.warning(request, 'Por favor, acesse sua conta primeiro')
        return redirect('acessar_conta')
 
    movimentos = conta.movimento_set.all().order_by('-data')[:5]
 
    return render(request, 'pages/conta.html', {'conta':conta, 'movimentos': movimentos})
 

def depositar(request, conta_id):
    conta = get_object_or_404(Conta, id=conta_id)
 
    
    if 'conta_numero' not in request.session or request.session['conta_numero'] != conta.numero:
        messages.warning(request, 'Por favor, acesse sua conta primeiro')
        return redirect('acessar_conta')
 
    
   
 
    if request.method == "POST":
        try:
            valor = Decimal(request.POST.get('valor_form')) 
            if valor > 0:
                l
                conta.depositar(valor)
                
                Movimento.objects.create(conta=conta, tipo='deposito', valor=valor)          
                messages.success(request, f"Depósito de R${valor:.2f} realizado!")
                
                return redirect('conta', conta_id=conta.id)
            else:
                messages.error(request, 'Valor invalido!')
        except:
            messages.error(request, 'Valor invalido!')
 
 
    return render(request, 'pages/depositar.html', {'conta': conta})
 
def sacar(request, conta_id):
    conta = get_object_or_404(Conta, id=conta_id)
 
    
    if 'conta_numero' not in request.session or request.session['conta_numero'] != conta.numero:
        messages.warning(request, 'Por favor, acesse sua conta primeiro')
        return redirect('acessar_conta')  
 
    
    if request.method == "POST":
        try:
            valor = Decimal(request.POST.get('valor_form'))
 
            
 
            if valor > 0 and conta.sacar(valor):
                
                Movimento.objects.create(conta=conta, tipo='saque', valor=valor)
                messages.success(request, f"Saque de R$ {valor:.2f} reaizado!")
                return redirect('conta', conta_id=conta.id)
            else:
                messages.error(request, 'Saldo insuficiente ou Valor invalido!')
        except:
            messages.error(request, 'Saldo insuficiente ou Valor invalido!')
   
    return render(request, 'pages/sacar.html', {'conta':conta})
   
def acessar_conta(request):
    
    if request.method == "POST":
        numero_conta = request.POST.get('numero_form')
        cpf_cliente = request.POST.get('cpf_form')
 
        cpf_limpo = cpf_cliente.replace('.', '').replace('-', '').replace(' ','')
 
        try:
            conta = Conta.objects.get(numero=numero_conta) 
            usuario = conta.cliente 
 
            if usuario.cpf != cpf_limpo:
                messages.error(request, 'CPF não correposnde ao número da conta')
                
                return render(request, 'pages/acessar_conta.html')
           

            request.session['conta_numero'] = numero_conta
            messages.success(request, f"Bem vindo de volta, {conta.cliente.nome}")
           
            #Direciona para a conta
            return redirect('conta', conta_id=conta.id)
       
        except Conta.DoesNotExist:
            messages.error(request, 'Conta não encontrada! Verifique o numero.')
   
    return render(request, 'pages/acessar_conta.html')
 
def logout(request):
    #Encerra toda sessao que exista
    request.session.flush()
    messages.info(request, 'Você saiu da conta!')
    return redirect("inicio")
 
 
 
 
 

   
   
   
   
  
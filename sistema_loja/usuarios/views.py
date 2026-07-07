from django.shortcuts import render,redirect, get_object_or_404
from django.urls import reverse
from rolepermissions.decorators import has_permission_decorator
from .models import Users
from django.http import HttpResponse
from django.contrib import auth
from django.contrib import messages


@has_permission_decorator('cadastrar_vendedor')
def cadastrar_vendedor(request):
    if request.method == 'GET':
        vendedores = Users.objects.filter(cargo='V')
        return render(request, 'cadastrar_vendedor.html',{'vendedores':vendedores})
    if request.method == 'POST':
        email = request.POST.get('email')
        senha = request.POST.get('senha')

        user = Users.objects.filter(email=email)
        if user.exists():
            messages.add_message(request,messages.WARNING, '❌ Email já existe em nosso banco de dados!')
            return redirect(reverse('cadastrar_vendedor'))
        
        user = Users.objects.create_user(username=email, email=email, password=senha, cargo= 'V')

        messages.add_message(request,messages.SUCCESS, '✅ Vendedor cadastrado com sucesso!')
        return redirect(reverse('cadastrar_vendedor'))
    

def login(request):
    if request.method == 'GET':
        if request.user.is_authenticated:
            return redirect(reverse('home'))
        return render(request, 'login.html')
    
    elif request.method == 'POST':
        login = request.POST.get('email')
        senha = request.POST.get('senha')
        
        user = auth.authenticate(username=login, password=senha)
    
        if not user:
            messages.add_message(request,messages.WARNING , '❌ Usuário Inválido!')
            return redirect(reverse('login'))
        
        auth.login(request, user)
        return HttpResponse('Logado com sucesso')
    
def logout(request):
    request.session.flush()
    messages.add_message(request,messages.WARNING , '❌ Deslogado.')
    return redirect(reverse('login'))

@has_permission_decorator('cadastrar_vendedor')        
def excluir_usuario(request, id):
    vendedor = get_object_or_404(Users, id=id)
    vendedor.delete()
    messages.add_message(request,messages.SUCCESS, '✅ Vendedor excluido com sucesso!')
    return redirect(reverse('cadastrar_vendedor'))
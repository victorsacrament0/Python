from django.shortcuts import render,redirect
from django.urls import reverse
from rolepermissions.decorators import has_permission_decorator
from .models import Users
from django.http import HttpResponse
from django.contrib import auth
@has_permission_decorator('cadastrar_vendedor')
def cadastrar_vendedor(request):
    if request.method == 'GET':
        return render(request, 'cadastrar_vendedor.html')
    if request.method == 'POST':
        email = request.POST.get('email')
        senha = request.POST.get('senha')

        user = Users.objects.filter(email=email)
        if user.exists():
            return HttpResponse('Email existente')
        
        user = Users.objects.create_user(username=email, email=email, password=senha, cargo= 'V')

        return HttpResponse('Conta criada')
    

def login(request):
    if request.method == 'GET':
         if request.user.is_authenticated:
            return redirect(reverse('home'))
    elif request.method == 'POST':
        email = request.POST.get('email')
        senha = request.POST.get('senha')
        
        user = auth.authenticate(username=login, password=senha)
        if not user:
            return HttpResponse('Usuário Inválido')
        
        auth.login(request, user)
        return HttpResponse('Logado com sucesso')
    
def logout(request):
    request.session.flush()
    return redirect(reverse('login'))
        
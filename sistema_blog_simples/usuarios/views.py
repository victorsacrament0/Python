from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import CadastroUsuarioForm
def cadastrar(request):
    if request.method == 'POST':
        form = CadastroUsuarioForm(request.POST)
        if form.is_valid():
            form.save()
            usuario = form.cleaned_data.get('usuario')
            messages.success(request, f'Conta criada com sucesso para {usuario}')
    else:
        form = CadastroUsuarioForm()
    return render(request,'usuarios/cadastrar.html',{'form':form})

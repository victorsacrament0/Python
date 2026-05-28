from django.shortcuts import render

from django.http import HttpResponse
# Create your views here.

def hello(request):
    return HttpResponse('<h1>Olá Mundo!</h1>'  '<p>olá Django</p>')

def contact(request):
    
    return render(request, 'clientes/contact.html')

def clientdb (request):
    titulo = 'Nossos Clientes'
    lista_clientes = {
        'nome:' : 'Thyago', 
        'idade' : '44',
        'nascimento' : '15/02/1982',
    }
    nome_clientes = ['Maria','Jose','Pedro','Ana']
    return render(request, 'clientes/home.html', {'mensagem':titulo, 'clientesdb':lista_clientes, 'dados':nome_clientes})
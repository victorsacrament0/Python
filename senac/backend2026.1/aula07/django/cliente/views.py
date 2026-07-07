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
    carros = [
        {'marca': "Chevrolet", 'modelo':'Onix LT', 'ano': '2020'},
        {'marca': "Fiat", 'modelo':'Uno', 'ano': '2010'},
        {'marca': "VW", 'modelo':'Gol', 'ano': '2022'},
    ]
    return render(request, 'clientes/home.html', {'mensagem':titulo, 'clientesdb':lista_clientes, 'dados':nome_clientes, 'meus_carros':carros})
from django.shortcuts import render



def dados_clientes (request):
    titulo = 'Nossos Clientes'
    
    lista_clientes = [
        {'nome' : 'Thyago','idade' : '44','nascimento' : '15/02/1982'},
        {'nome' : 'João','idade' : '22','nascimento' : '11/03/2004'},
        {'nome' : 'Marcela','idade' : '20','nascimento' : '22/04/2006'},
    ]

    return render(request, 'clientes\dados_clientes.html', { 'mensagem':titulo, 'clientesdb':lista_clientes })
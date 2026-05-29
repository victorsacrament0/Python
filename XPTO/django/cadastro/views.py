from django.shortcuts import render



def dados_alunos (request):
    titulo = 'Nossos Alunos'
    
    lista_alunos = [
        {'nome' : 'Thyago Matarazzo','curso' : 'Análise e Desenvolvimento de Sistemas','turma' : '2026.2Ma'},
        {'nome' : 'João Gutierrez','curso' : 'Ciência da Computação','turma' : '2026.1T'},
        {'nome' : 'Marcela Correa','curso' : 'Engenharia de Software','turma': '2026.1N'},
    ]

    return render(request, 'clientes\dados_clientes.html', { 'mensagem':titulo, 'clientesdb':lista_alunos })
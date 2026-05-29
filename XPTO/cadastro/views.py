from django.shortcuts import render

# Create your views here.


def dados_alunos (request):
    titulo = 'Nossos Alunos'
    
    lista_alunos = [
        {'nome' : 'Thyago Matarazzo','curso' : 'Análise e Desenvolvimento de Sistemas','turma' : '2026.2M'},
        {'nome' : 'João Gutierrez','curso' : 'Ciência da Computação','turma' : '2026.1T'},
        {'nome' : 'Marcela Correa','curso' : 'Engenharia de Software','turma': '2026.1N'},
        {'nome' : 'Pedro Pereira','curso' : 'Sistemas de Informação','turma': '2026.2N'},
    ]

    return render(request, 'alunos\dados_alunos.html', { 'mensagem':titulo, 'clientesdb':lista_alunos })
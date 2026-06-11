from django.shortcuts import render
from .models import Aluno, Campus
# Create your views here.

def home (request):
    titulo = 'XPTO Tecnologias'
    return render(request, 'alunos/home.html', {'titulo':  titulo})

def dados_alunos (request):
    titulo = 'Nossos Alunos'
    
    lista_alunos = Aluno.objects.all()

    return render(request, 'alunos\dados_alunos.html', { 'mensagem':titulo, 'lista_alunos':lista_alunos })

def campus(request):
    titulo = "Unidades Escolares"
    nossos_campus = Campus.objects.all()
    return render(request, 'alunos\campus.html', { 'titulo': titulo, 'nossos_campus':nossos_campus })
from django.shortcuts import render, redirect
from django.http import HttpResponse
from usuario.models import Usuario
from .models import Livros, Categoria,Emprestimo
from .forms import CadastroLivro

def home(request):
    if request.session.get('usuario'):
        usuario = Usuario.objects.get(id = request.session['usuario'])
        livros = Livros.objects.filter(usuario=usuario)
        form = CadastroLivro()
        return render(request,'home.html',{'livros':livros,'form':form, 'usuario_logado': request.session.get('usuario')})    
    else:
        return redirect ('/auth/login/?status=2')
    
def ver_livro(request,id):
    if request.session.get('usuario'):
        livro = Livros.objects.get(id=id)
        if request.session.get('usuario') == livro.usuario.id:
            categoria_livro = Categoria.objects.filter(usuario_id = request.session.get('usuario'))
            emprestimos = Emprestimo.objects.filter(livro=livro)
            form = CadastroLivro()
            return render(request,'ver_livro.html', {'livro':livro, 'form':form,'categoria_livro':categoria_livro,'emprestimos':emprestimos ,'usuario_logado': request.session.get('usuario')})
        else:
            return HttpResponse('Esse livro não é seu!')    
    return redirect ('/auth/login/?status=2')


def cadastrar_livro(request):
    if request.method == 'POST':
        form = CadastroLivro(request.POST)
        livro = Livros(
            nome = form.data['nome'],
            autor = form.data['autor'],
            co_autor = form.data['co_autor'],
            data_cadastro = form.data['data_cadastro'],
            emprestado = form.data['emprestado'],
            categoria = form.data['categoria'],
        )
        return HttpResponse('teste')
    return HttpResponse('teste')
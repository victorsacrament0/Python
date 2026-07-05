from django.shortcuts import render, redirect
from django.http import HttpResponse
from usuario.models import Usuario
from .models import Livros, Categoria,Emprestimo
from .forms import CadastroLivro,CategoriaLivro
from django import forms
from datetime import datetime
from django.db.models import Q

def home(request):
    if request.session.get('usuario'):
        usuario = Usuario.objects.get(id = request.session['usuario'])
        usuarios = Usuario.objects.all()
        status_categoria = request.GET.get('cadastro_categoria')
        livros = Livros.objects.filter(usuario=usuario)
        livros_emprestar = Livros.objects.filter(usuario=usuario).filter(emprestado = False)
        livros_emprestados = Livros.objects.filter(usuario=usuario).filter(emprestado = True)
        total_livros = livros.count
        form = CadastroLivro()
        form_categoria = CategoriaLivro()
        form.fields['usuario'].initial = request.session['usuario']
        form.fields['categoria'].queryset = Categoria.objects.filter(usuario = usuario)
        return render(request,'home.html',{'livros':livros,
                                           'livros_emprestar':livros_emprestar,
                                           'livros_emprestados':livros_emprestados,
                                           'total_livros':total_livros,
                                           'form':form,
                                           'usuarios':usuarios, 
                                           'form_categoria':form_categoria, 
                                           'status_categoria':status_categoria,
                                           'usuario_logado': request.session.get('usuario')})    
    else:
        return redirect ('/auth/login/?status=2')
    
def ver_livro(request,id):
    if request.session.get('usuario'):
        livro = Livros.objects.get(id=id)
        if request.session.get('usuario') == livro.usuario.id:
            usuario = Usuario.objects.get(id = request.session['usuario'])
            usuarios = Usuario.objects.all()
            livros_emprestar = Livros.objects.filter(usuario=usuario).filter(emprestado = False)
            livros_emprestados = Livros.objects.filter(usuario=usuario).filter(emprestado = True)
            categoria_livro = Categoria.objects.filter(usuario_id = request.session.get('usuario'))
            emprestimos = Emprestimo.objects.filter(livro=livro)
            form = CadastroLivro()
            form.fields['usuario'].initial = request.session['usuario']
            form.fields['categoria'].queryset = Categoria.objects.filter(usuario = usuario)
            form_categoria = CategoriaLivro()
            return render(request,'ver_livro.html', {'livro':livro,
                                                     'livros_emprestar':livros_emprestar, 
                                                     'livros_emprestados':livros_emprestados,
                                                     'form':form, 
                                                     'usuarios':usuarios,
                                                     'id_livro':id,
                                                     'form_categoria':form_categoria,
                                                     'categoria_livro':categoria_livro,
                                                     'emprestimos':emprestimos,
                                                     'usuario_logado': request.session.get('usuario')
                                                     })
        else:
            return redirect('/livro/home')   
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
        return redirect('/livro/home')
    return redirect('/livro/home')

def excluir_livro(self,id_livro):
    livro = Livros.objects.get(id=id).delete()
    return redirect('/livro/home')

def cadastrar_categoria (request):
    form = CategoriaLivro(request.POST)
    nome = form.data['nome']
    descricao = form.data['descricao']
    id_usuario = request.POST.get('usuario')
    
    if int(id_usuario) == int(request.session.get('usuario')):
        user = Usuario.objects.get(id= id_usuario)
        categoria = Categoria(nome = nome, 
                              descricao = descricao, 
                              usuario= user 
                            )
        categoria.save()
        return redirect ('/livro/home?cadastro_categoria=1')
    return redirect ('/livro/home?cadastro_categoria=2')

def cadastrar_emprestimo(request):
    if request.method == 'POST':
        nome_emprestado = request.POST.get('nome_emprestado')
        livro_emprestado = request.POST.get('livro_emprestado')

        emprestimo = Emprestimo(nome_emprestado_id = nome_emprestado, livro_id = livro_emprestado)
        emprestimo.save()

        livro = Livros.objects.get(id= livro_emprestado)
        livro.emprestado = True
        livro.save()

        return redirect('/livro/home')
    
def devolver_livro (request):
    id = request.POST.get('id_devolver')
    livro_devolver = Livros.objects.get(id = id)
    livro_devolver.emprestado = False
    livro_devolver.save()
    emprestimo_devolver = Emprestimo.objects.get(Q(livro = livro_devolver) & Q(data_devolucao = None))
    emprestimo_devolver.data_devolucao = datetime.now()
    emprestimo_devolver.save()
    
    return redirect('/livro/home')

def alterar_livro(request):
    livro_id = request.POST.get('livro_id')
    nome_livro = request.POST.get('nome_livro')
    autor = request.POST.get('autor')
    co_autor = request.POST.get('co_autor')
    categoria_id = request.POST.get('categoria_id')

    categoria = Categoria.objects.get(id=categoria_id)
    livro = Livros.objects.get(id = livro_id)
    if livro.usuario.id == request.session['usuario']:
        livro.nome = nome_livro
        livro.autor = autor
        livro.co_autor = co_autor
        livro.categoria = categoria
        livro.save()
        return redirect('/livro/ver_livro/{livro_id}')
    return redirect('/livro/home')

def seus_emprestimos(request):
    usuario = Usuario.objects.get(id = request.session['usuario'])
    emprestimos = Emprestimo.objects.filter(nome_emprestado = usuario)
    
    return render(request, 'seus_emprestimos.html', {'usuario_logado':request.session['usuario'], 'emprestimos':emprestimos})
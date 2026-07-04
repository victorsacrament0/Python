from django.shortcuts import render, redirect
from django.http import HttpResponse
from usuario.models import Usuario
from .models import Livros, Categoria,Emprestimo
from .forms import CadastroLivro,CategoriaLivro

def home(request):
    if request.session.get('usuario'):
        usuario = Usuario.objects.get(id = request.session['usuario'])
        status_categoria = request.GET.get('cadastro_categoria')
        livros = Livros.objects.filter(usuario=usuario)
        form = CadastroLivro()
        form_categoria = CategoriaLivro()
        form.fields['usuario'].initial = request.session['usuario']
        form.fields['categoria'].queryset = Categoria.objects.filter(usuario = usuario)
        return render(request,'home.html',{'livros':livros,'form':form, 'form_categoria':form_categoria, 'usuario_logado': request.session.get('usuario')})    
    else:
        return redirect ('/auth/login/?status=2')
    
def ver_livro(request,id):
    if request.session.get('usuario'):
        livro = Livros.objects.get(id=id)
        if request.session.get('usuario') == livro.usuario.id:
            usuario = Usuario.objects.get(id = request.session['usuario'])
            categoria_livro = Categoria.objects.filter(usuario_id = request.session.get('usuario'))
            emprestimos = Emprestimo.objects.filter(livro=livro)
            form = CadastroLivro()
            form.fields['usuario'].initial = request.session['usuario']
            form.fields['categoria'].queryset = Categoria.objects.filter(usuario = usuario)
            form_categoria = CategoriaLivro()
            return render(request,'ver_livro.html', {'livro':livro, 
                                                     'form':form, 
                                                     'id_livro':id,
                                                     'form_categoria':form_categoria,
                                                     'categoria_livro':categoria_livro,
                                                     'emprestimos':emprestimos ,
                                                     'usuario_logado': request.session.get('usuario')
                                                     })
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
        return redirect('/livro/home')
    return redirect('/livro/home')

def excluir_livro(self,id_livro):
    livro = Livros.objects.get(id=id).delete()
    return redirect('/livro/home')

def cadastrar_categoria (request):
    form = CategoriaLivro(request.POST)
    nome = form.data['nome']
    descicao = form.data['descicao']
    id_usuario = request.POST.get('usuario')
    
    if int(id_usuario) == int(request.session.get('usuario')):
        user = Usuario.objects.get(id= id_usuario)
        categoria = Categoria(nome = nome, 
                              descicao = descicao, 
                              usuario= user 
                            )
        categoria.save()
        return redirect ('/livro/home?cadastro_categoria=1')
    return redirect ('/livro/home?cadastro_categoria=2')
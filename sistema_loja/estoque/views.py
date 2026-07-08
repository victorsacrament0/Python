from rolepermissions.decorators import has_permission_decorator
from django.core.files.uploadedfile import InMemoryUploadedFile
from .models import Categoria,Produto, Imagem
from django.shortcuts import render,redirect
from .forms import ProdutoForm
from django.contrib import messages
from PIL import Image, ImageDraw
from django.urls import reverse
from datetime import date
from io import BytesIO
import sys



@has_permission_decorator('cadastrar_produto')
def add_produto (request):
    if request.method == 'GET':
        categorias = Categoria.objects.all()
        produtos = Produto.objects.all()
        return render (request, 'add_produto.html', {'categorias':categorias, 'produtos':produtos})

    elif request.method == 'POST':
        nome = request.POST.get('nome')
        categoria = request.POST.get('categoria')
        quantidade = request.POST.get('quantidade')
        preco_compra = request.POST.get('preco_compra')
        preco_venda = request.POST.get('preco_venda')

        produto = Produto(nome=nome, categoria_id=categoria, quantidade=quantidade, preco_compra=preco_compra, preco_venda=preco_venda)
        produto.save()

        for i in request.FILES.getlist('imagens'):
            name = f'{date.today()}-{produto.id}.jpg'
            img = Image.open(i)
            img = img.convert('RGB')
            img = img.resize((300,300))
            draw = ImageDraw.Draw(img)
            draw.text((20,280),'LojaPy', (255, 255, 255))
            output = BytesIO()
            img.save(output, format='JPEG', quality=100)
            output.seek(0)
            img_tratada = InMemoryUploadedFile(output, 'ImageField', name,'image/jpeg', sys.getsizeof(output),None)
            img_t = Imagem(imagem = img_tratada, produto=produto)
            img_t.save()
        messages.add_message(request,messages.SUCCESS, '✅ Produto cadastrado com sucesso!')
        return redirect(reverse('add_produto'))
    
def produto (request,slug):
    if request.method == 'GET':
        produto = Produto.objects.get(slug=slug)
        cat = produto.__dict__
        cat['categoria'] = produto.categoria.id
        form = ProdutoForm(initial=cat)
    return render(request, 'produto.html', {'form':form})
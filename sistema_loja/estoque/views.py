from django.shortcuts import render
from .models import Categoria,Produto, Imagem
from PIL import Image, ImageDraw
from datetime import date
from io import BytesIO
from django.core.files.uploadedfile import InMemoryUploadedFile
import sys
# Create your views here.

def add_produto (request):
    if request.method == 'GET':
        categorias = Categoria.objects.all()
        return render (request, 'add_produto.html', {'categorias':categorias})

    elif request.method == 'POST':
        nome = request.POST.get('nome')
        categoria = request.POST.get('categoria')
        quantidade = request.POST.get('quantidade')
        preco_compra = request.POST.get('preco_compra')
        preco_venda = request.POST.get('preco_venda')
        imagens = request.FILES.getlist('imagens')

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
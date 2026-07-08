from atexit import register
from django import template
from estoque.models import Imagem

register = template.Library()

@register.filter(name='get_first_image')    
def get_first_image(product):
    imagem = Imagem.objects.filter(produto=product).first()
    return imagem.imagem.url
from django import template
from datetime import date, datetime

register = template.Library()

@register.filter
def  mostra_duracao(value1,value2):
    
    if all((isinstance(value1,datetime)),(isinstance(value2,datetime))):
        return f'{(value1 - value2).days}  dia(s)'
    
    return '⌛'
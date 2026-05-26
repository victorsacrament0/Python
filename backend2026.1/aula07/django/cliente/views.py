from django.shortcuts import render

from django.http import HttpResponse
# Create your views here.

def hello(request):
    return HttpResponse('<h1>Olá Mundo!</h1>'  '<p>olá Django</p>')

def contact(request):
    return HttpResponse('<h2>Contato</h2><br><form><input type="email" placeholder="email@email.com.br"><br><input type=text placeholder="99 99999-9999"></form><br><button><b>Entrar</b></button>')


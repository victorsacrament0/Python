from django.shortcuts import render
from .models import Postagem

def home(request):
    context ={
        'posts': Postagem.objects.all()
    }
    return render(request, "pages/home.html", context)

def sobre(request):
    return render(request, "pages/sobre.html")

from django.contrib import admin
from django.urls import path
from cadastro.views import dados_alunos, home,campus

urlpatterns = [
    path('',home,name='/'),
    path('admin/', admin.site.urls),
    path('alunos/', dados_alunos, name='alunos'),
    path('unidades/', campus , name='unidades'),
]

from django.shortcuts import render, redirect
from .models import Pacientes
from django.contrib import messages
from django.contrib.messages import constants

def pacientes(request):
    if request.method == 'GET':
        pacientes = Pacientes.objects.all()
        queixas = Pacientes.queixa_choices
        return render(request,'pacientes.html', {'queixas': queixas,'pacientes':pacientes})
    elif request.method == 'POST':
        nome = request.POST.get('nome')
        email = request.POST.get('email')
        telefone = request.POST.get('telefone')
        queixa = request.POST.get('queixa')
        foto = request.FILES.get('foto')

        if len(nome.strip()) == 0 or not foto:
            messages.add_message(request, constants.ERROR, 'Preencha todos os campos')
            return redirect('pacientes')

        paciente = Pacientes(
            nome=nome,
            email=email,
            telefone=telefone,
            queixa=queixa,
            foto=foto
        )

        paciente.save()
        messages.add_message(request, constants.SUCCESS, 'Cadastro realizado com sucesso!')
        return redirect('pacientes') 
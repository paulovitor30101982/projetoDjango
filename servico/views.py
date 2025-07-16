from django.shortcuts import render, redirect
from .models import Servico

def cadastrar_servico(request):
    if request.method == 'POST':
        nome = request.POST.get('nome')
        preco = request.POST.get('preco')
        descricao = request.POST.get('descricao')

        Servico.objects.create(
            nome=nome,
            preco=preco,
            descricao=descricao
        )
        return redirect('/servicos')  # ou redirecionar para outra página

    return render(request, 'cadastroServico.html')

def listar_servicos(request):
    servicos = Servico.objects.all()
    return render(request, 'listaServicos.html', {'servicos': servicos})



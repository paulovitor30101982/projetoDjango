from django.shortcuts import render, redirect
from django.http import HttpResponseForbidden
from .models import Produto

def cadastrar_produto(request):
    if not request.user.has_perm('cadastroP.add_produto'):
        return HttpResponseForbidden("Você não tem permissão para cadastrar produtos.")

    if request.method == 'POST':
        nome = request.POST.get('nome')
        preco = request.POST.get('preco')
        descricao = request.POST.get('descricao')

        Produto.objects.create(
            nome=nome,
            preco=preco,
            descricao=descricao
        )
        return redirect('/produtos')  # ou qualquer outro destino

    return render(request, 'cadastroProdutos.html')

def listar_produtos(request):
    produtos = Produto.objects.all()
    return render(request, 'listaProdutos.html', {'produtos': produtos})


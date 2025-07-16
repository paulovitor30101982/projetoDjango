from django.shortcuts import render, redirect
from django.contrib.auth.models import User

def cadastrar_usuario(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')

        if User.objects.filter(username=username).exists():
            return render(request, 'cadastro.html', {'erro': 'Usuário já existe'})

        User.objects.create_user(username=username, email=email, password=password)
        return redirect('login')

    return render(request, 'cadastro.html')

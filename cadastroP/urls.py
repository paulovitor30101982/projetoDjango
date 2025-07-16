from django.urls import path
from .views import cadastrar_produto, listar_produtos

urlpatterns = [
    path('cadastro/', cadastrar_produto, name='cadastrar_produto'),
    path('', listar_produtos, name='listar_produtos'),
]

from django.urls import path
from .views import cadastrar_servico, listar_servicos

urlpatterns = [
    path('cadastro/', cadastrar_servico, name='cadastrar_servico'),
    path('', listar_servicos, name='listar_servicos'),
]

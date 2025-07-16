from django.contrib import admin
from django.urls import path, include 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('frutas/', include('app01.urls')),
    path('livros/', include('app02.urls')),     
    path('produtos/', include('cadastroP.urls')),
    path('servicos/', include('servico.urls')),
    path('usuarios/', include('cadastroUser.urls')),
    path('login/', include('login.urls')),
]

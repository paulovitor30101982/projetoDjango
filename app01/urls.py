from django.urls import path
from .views import lista_frutas

urlpatterns = [
    path('', lista_frutas),    
]

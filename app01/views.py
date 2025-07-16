from django.shortcuts import render

# Create your views here.

def lista_frutas(request):
   frutas = ['Maçã', 'Banana', 'Laranja','Abacaxi']
   return render(request, 'lista_frutas.html', {'frutas':frutas}) 

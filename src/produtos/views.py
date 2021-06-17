# from django.shortcuts import render
from django.db.models.fields import NullBooleanField
import produtos
from django.views.generic import DetailView, ListView
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, request, response
from .models import Produtos

def post_list(request):
    # pega todos os objetos de Produtos em ordem e adiciona a variavel produtos;
    produtos = Produtos.objects.all().order_by('-created')

    # retorna a pagina index.html com o objeto "produtos", isso siguinifica que 
    # posso usar o objeto "produtos" na pagina index.html
    return render(request, 'index.html', {'produtos':produtos})

def post_about(request):
    return render(request, 'about.html')

def post_services(request):
    return render(request, 'services.html')    

def post_detalhes(request, id):
    produtos = Produtos.objects.get(id=id)
    if request.method == 'GET':
        return render(request, 'work-single.html', {'produtos':produtos})
    
    
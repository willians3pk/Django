from django.db import models
from django.contrib.auth.models import User


class Produtos(models.Model):
    
    nome = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True)
    preco = models.CharField(max_length=10)
    tamanho = models.CharField(max_length=10, blank=True)
    foto = models.ImageField(upload_to="img/")
    descricao = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)
#   author = models.ForeignKey(User, on_delete=models.CASCADE)

from django.db import models
from marca.models import Marca

class Produto(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField()
    marca = models.ForeignKey(Marca, on_delete=models.CASCADE)
    preco = models.FloatField()
    imagem = models.ImageField(upload_to="images")
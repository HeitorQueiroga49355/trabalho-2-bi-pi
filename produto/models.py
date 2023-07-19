from django.db import models

# Create your models here.
class Marca(models.Model):
    nome = models.CharField(max_length=50)
    logo = models.ImageField(upload_to="images")

class Produto(models.Model):
    nome = models.CharField(max_length=100)
    marca = models.ForeignKey(Marca, on_delete=models.CASCADE)
    preco = models.FloatField()
    imagem = models.ImageField(upload_to="images")
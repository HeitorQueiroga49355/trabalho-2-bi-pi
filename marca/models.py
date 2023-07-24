from django.db import models

class Marca(models.Model):
    nome = models.CharField(max_length=50)
    logo = models.ImageField(upload_to="images")

    def __str__(self):
        return self.nome
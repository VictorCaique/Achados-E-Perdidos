from django.db import models

class ItemPerdido(models.Model):
    descricao = models.fields.TextField(max_length=1000)
    data_encontrado = models.fields.DateField()
    image_uri = models.fields.CharField(max_length=500)
    titulo = models.fields.CharField(max_length=255)

    def __str__(self) -> str:
        return self.descricao

class Requesicao(models.Model):
    nome = models.fields.CharField(max_length=255)
    email = models.fields.EmailField()
    telefone = models.fields.CharField(max_length=12)
    data_perdido = models.fields.DateField()
    mensagem = models.fields.TextField(max_length=2000)

# Create your models here.

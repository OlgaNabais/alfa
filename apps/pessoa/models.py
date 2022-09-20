from django.db import models

# Create your models here.
# Vamos começar por criar modelos:

class Pessoa(models.Model): # vao ter esta herança dentro do modelo
    nome = models.CharField(max_length=50) # extenção de 50 caracteres
    idade = models.IntegerField() # verbose_name="idade"
    nif = models.CharField(max_length=9)
    email = models.EmailField()

# vamos fazer uma função que herda desta classe
    def __str__(self):
        return f'Nome: {self.nome}'
from django.db import models

# Create your models here.
class Animal(models.Model):
    nome = models.CharField(max_length=50)
    especie = models.CharField(max_length=30)
    idade = models.IntegerField()

    def __str__(self):
        return f'{self.especie}: {self.nome}'
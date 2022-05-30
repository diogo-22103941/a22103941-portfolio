import imp

from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Post(models.Model):
    autor = models.CharField(max_length=100)
    data = models.DateTimeField(auto_now_add=True)
    titulo = models.CharField(max_length=100)
    descricao = models.TextField()

    def __str__(self):
        return self.titulo[:20] + '...'


class PontuacaoQuizz(models.Model):
    nome = models.CharField(unique=True, max_length=50)
    pontos = models.PositiveIntegerField()


class Cadeira(models.Model):
    nome = models.CharField(max_length=50)
    ano = models.IntegerField(validators=[MinValueValidator(1),
                                          MaxValueValidator(3)])
    semestre = models.IntegerField(validators=[MinValueValidator(1),
                                               MaxValueValidator(2)])
    ects = models.IntegerField(validators=[MinValueValidator(1),
                                           MaxValueValidator(6)])

    def __str__(self):
        return self.nome[:30] + '...'


class Projeto(models.Model):
    titulo = models.CharField(max_length=50)
    descricao = models.TextField(max_length=500)
    ano_realizacao = models.IntegerField(validators=[MinValueValidator(1),
                                                     MaxValueValidator(3)])
    cadeira = models.ForeignKey(Cadeira, on_delete=models.DO_NOTHING, blank=True, null=True)

    def __str__(self):
        return self.titulo[:50]

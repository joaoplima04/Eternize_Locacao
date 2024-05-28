from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractUser

class Produto(models.Model):

    OPCOES_CATEGORIA = [
        ("PRATO RASO", "Prato Raso"),
        ("GUARDANAPO", "Guardanapo"),
        ("TALHER", "Talher"),
        ("TACAS", "Tacas"),
        ("TRILHOS DE MESA", "Trilhos de Mesa"),
        ("SOUPLAT", "Souplat"),
        ("JOGO AMERICANO", "Jogo Americano"),
        ("CHA E CAFE", "Cha e Cafe"),
        ("PRATO SOBREMESA", "Prato Sobremesa"),
        ("PORTA GUARDANAPO", "Porta Guardanapo"),
    ]

    OPCOES_ESTILO = [
        ("ELEGANTE", "Elegante"),
        ("TROPICAL", "Tropical"),
        ("FLORIDO", "Florido"),
    ]

    nome = models.CharField(max_length=100)
    categoria = models.CharField(max_length=150, choices=OPCOES_CATEGORIA, default='')
    preco = models.DecimalField(decimal_places=2, max_digits=10)
    quantidade_estoque = models.IntegerField(null=False, blank=False, default=0)
    imagem = models.ImageField(upload_to="imagens/", blank=True)
    cor = models.CharField(max_length=100)
    estilo = models.CharField(max_length=100, choices=OPCOES_ESTILO, default='')
    estoque = models.IntegerField(null=False, blank=False)

def __str__(self):
    return self.nome

class Cliente(AbstractUser):
    cpf = models.CharField(max_length=11, primary_key=True, default='')
    username = models.CharField(max_length=150, unique=True) 
    nome = models.CharField(max_length=100)
    email = models.EmailField()  
    telefone = models.CharField(max_length=20)  
    data_nascimento = models.DateField(default=timezone.now)  
    senha = models.CharField(max_length=100)


    def __str__(self):
        return self.nome

class Aluguel(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    data_aluguel = models.DateField(default=timezone.now)
    data_devolucao = models.DateField()
    preco_total = models.DecimalField(decimal_places=2, max_digits=10)
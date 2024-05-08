from django.db import models
from django.utils import timezone

class Produto(models.Model):
    nome = models.CharField(max_length=100)
    categoria = models.CharField(max_length=100)
    preco = models.DecimalField(decimal_places=2, max_digits=10)
    quantidade_estoque = models.IntegerField
    imagem = models.CharField(max_length=100)
    cor = models.CharField(max_length=100)

def __str__(self):
    return self.nome

class Cliente(models.Model):
    cpf = models.CharField(max_length=11, primary_key=True, default='11111111111') 
    nome = models.CharField(max_length=100)
    email = models.EmailField()  
    telefone = models.CharField(max_length=20)  
    data_nascimento = models.DateField(default=timezone.now)  


    def __str__(self):
        return self.nome

class Aluguel(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    data_aluguel = models.DateField(default=timezone.now)
    data_devolucao = models.DateField()
    preco_total = models.DecimalField(decimal_places=2, max_digits=10)

class ItemAluguel(models.Model):
    aluguel = models.ForeignKey(Aluguel, on_delete=models.CASCADE)
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE)
    quantidade = models.PositiveIntegerField(default=1)
    preco_item = models.DecimalField(decimal_places=2, max_digits=10)
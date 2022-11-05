from django.db import models

# Create your models here.

class Status(models.IntegerChoices):
    Criado = 1
    Efetuado = 2
    Entregue = 3


class Produto(models.Model):
    id = models.IntegerField()
    codigo = models.CharField()
    nome = models.CharField()
    ingredientes = models.TextField()
    descricao = models.TextField()
    valor = models.DecimalField()

class MetodosPagamento(models.Model):
    id = models.IntegerField()
    descricao = models.TextField()

class ItemPedido(models.Model):
    id = models.IntegerField()
    codigo = models.CharField()
    quantidade = models.IntegerField()
    observacao = models.TextField()
        

class Pedido(models.Model):
    id = models.IntegerField()
    codigo = models.CharField()
    pago = models.BooleanField()
    valorTotal = models.DecimalField()
    metodoPagamentoId = user = models.ForeignKey(
        MetodosPagamento, on_delete=models.CASCADE, related_name="id"
    )
    nomeCliente = models.CharField()
    telefone = models.CharField()
    endereco = models.CharField()
    horarioPedido = models.DateTimeField()
    status = models.IntegerChoices(choices=Status.choices)
    observacao = models.TextField()
    entrega = models.BooleanField()
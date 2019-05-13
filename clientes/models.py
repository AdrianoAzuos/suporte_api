from django.db import models

# Create your models here.
class Tipo(models.Model):
    nome = models.CharField(max_length=80,null=False,blank=False,unique=True)
    descricao = models.CharField(max_length=255,null=False,blank=False)
    def __str__(self):
        return self.nome
class Cliente(models.Model):
    nome_completo = models.CharField(max_length=80,null=False,blank=False)
    info = models.TextField(blank=True, null=True)
    tipo = models.ForeignKey(Tipo, on_delete=models.CASCADE)
    data_cadastro = models.DateField(auto_now_add=True)
    def __str__(self):
        return self.nome_completo
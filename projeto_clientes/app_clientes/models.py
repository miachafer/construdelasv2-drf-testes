from django.db import models

'''
Modelo Cliente simples com apenas um método string que retorna o atributo nome
'''

class Cliente(models.Model):
    nome = models.CharField(max_length=50)
    idade = models.IntegerField(default=0)
    rg = models.CharField(max_length=13)
    email = models.EmailField()
    telefone = models.IntegerField()

    def __str__(self):
        return self.nome    

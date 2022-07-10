from rest_framework import serializers
from .models import Cliente

'''Classe serializadora que contempla todos os atributos do modelo Cliente'''

class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = ('nome', 'idade', 'rg', 'email', 'telefone')

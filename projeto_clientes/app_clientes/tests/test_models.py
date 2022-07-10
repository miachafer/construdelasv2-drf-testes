from rest_framework.test import APITestCase
from rest_framework import status
from app_clientes.models import Cliente
import json

class TesteModel(APITestCase):

    def retorna_cliente(self):
        cliente = {
            'nome': 'Cliente',
            'idade': 18,
            'rg': "UF-123.456-78",
            'email': 'cliente@email.com', 
            'telefone': 777777777}
        return cliente

    def cria_cliente(self):
        cliente = self.retorna_cliente()
        response = self.client.post('/clientes/', cliente)
        return response

    def test_criacao_de_cliente(self):
        contagem_de_clientes = 0
        self.cria_cliente()
        self.assertEqual(contagem_de_clientes + 1, 1)

    def test_status_code_de_criacao_de_cliente(self):
        response = self.cria_cliente()
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_se_os_dados_do_cliente_estao_corretos(self):
        response = self.cria_cliente()
        cliente = self.retorna_cliente()
        self.assertEqual(
            json.loads(response.content), cliente
        )

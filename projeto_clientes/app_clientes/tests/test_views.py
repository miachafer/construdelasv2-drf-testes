from rest_framework.test import APITestCase
from rest_framework import status
from app_clientes.models import Cliente

class TesteViews(APITestCase):

    def cria_cliente(self):
        cliente = {
            'nome': 'Cliente',
            'idade': 18,
            'rg': "UF-123.456-78",
            'email': 'cliente@email.com', 
            'telefone': 777777777}
        response = self.client.post('/clientes/', cliente)
        return response

    def test_se_url_clientes_funciona(self):
        response = self.client.get('/clientes/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_se_url_do_cliente_funciona(self):
        self.cria_cliente()
        cliente = Cliente.objects.get(nome='Cliente')
        response = self.client.get('/clientes/', args=cliente.pk)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    
    
# steps/carrinhos_steps.py

from behave import given, when, then
import requests
import random
from tests.config import BASE_URL

# Helpers
def get_auth_token():
    """Obtém token de autenticação"""
    response = requests.post(
        f"{BASE_URL}/login",
        json={"email": "fulano@qa.com", "password": "teste"},
        headers={"Content-Type": "application/json"}
    )
    return response.json()["authorization"]

def create_test_product():
    """Cria um produto de teste e retorna seu ID"""
    token = get_auth_token()
    product = {
        "nome": f"Produto Teste {random.randint(1000,9999)}",
        "preco": 100,
        "descricao": "Descrição do produto teste",
        "quantidade": 10
    }
    response = requests.post(
        f"{BASE_URL}/produtos",
        headers={
            "Authorization": token,
            "Content-Type": "application/json"
        },
        json=product
    )
    return response.json()["_id"]

def limpar_carrinho_existente(token):
    """Remove o carrinho existente se houver"""
    response = requests.get(
        f"{BASE_URL}/carrinhos",
        headers={"Authorization": token}
    )
    dados = response.json()
    if dados.get("carrinhos"):
        requests.delete(
            f"{BASE_URL}/carrinhos/concluir-compra",
            headers={"Authorization": token}
        )

# Steps
@given("que eu tenho um token de usuário válido")
def step_impl(context):
    context.token = get_auth_token()
    context.headers = {
        "Authorization": context.token,
        "Content-Type": "application/json"
    }
    limpar_carrinho_existente(context.token)

@given("um produto existente no catálogo")
def step_impl(context):
    context.product_id = create_test_product()
    context.payload = {
        "produtos": [{
            "idProduto": context.product_id,
            "quantidade": 1
        }]
    }

@given("um produto com ID inválido")
def step_impl(context):
    context.payload = {
        "produtos": [{
            "idProduto": "id_invalido_123",
            "quantidade": 1
        }]
    }

@when("eu faço uma requisição POST para /carrinhos")
def step_impl(context):
    context.response = requests.post(
        f"{BASE_URL}/carrinhos",
        headers=context.headers,
        json=context.payload
    )
    print(f"Resposta da API: {context.response.status_code} - {context.response.text}")

@then("o status code deve ser {status_code:d}")
def step_impl(context, status_code):
    atual = context.response.status_code
    corpo = context.response.text
    assert atual == status_code, f"Esperado: {status_code}, Recebido: {atual} - {corpo}"

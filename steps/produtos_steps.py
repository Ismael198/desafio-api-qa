from behave import *
import requests
import random
from tests.config import BASE_URL

@given('que o usuário esteja autenticado com "fulano@qa.com" e "teste"')
def step_impl(context):
    # Faz login para obter o token
    response = requests.post(
        f"{BASE_URL}/login",
        json={"email": "fulano@qa.com", "password": "teste"},
        headers={
            "accept": "application/json",
            "Content-Type": "application/json"
        }
    )

    assert response.status_code == 200, f"Falha no login: {response.text}"
    context.token = response.json()["authorization"]

    context.headers = {
        "Authorization": context.token,
        "accept": "application/json",
        "Content-Type": "application/json"
    }

@when('ele envia os dados do produto')
def step_impl(context):
    # Gera um nome único para o produto
    product_id = random.randint(1000, 9999)
    context.produto = {
        "nome": f"Logitech MX Vertical {product_id}",
        "preco": 470,
        "descricao": "Mouse",
        "quantidade": 381
    }

    context.response = requests.post(
        f"{BASE_URL}/produtos",
        headers=context.headers,
        json=context.produto
    )

@then('o produto é adicionado com sucesso')
def step_impl(context):
    print(f"Produto criado: {context.produto['nome']}")  # Debug
    print(f"Resposta: {context.response.text}")  # Debug
    assert context.response.status_code == 201, \
        f"Status code inesperado: {context.response.status_code}"
    assert context.response.json()["message"] == "Cadastro realizado com sucesso"
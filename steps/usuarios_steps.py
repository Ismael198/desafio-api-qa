from behave import *
import requests
import random
from tests.config import BASE_URL

@given("que eu tenho um novo usuário com email único")
def step_impl(context):
    context.payload = {
        "nome": "Usuário BDD",
        "email": f"usuario_{random.randint(1, 1000)}@qa.com",
        "password": "teste",
        "administrador": "true"
    }

@given("que eu tenho um usuário com email já existente")
def step_impl(context):
    context.payload = {
        "nome": "Usuário Existente",
        "email": "usuario_existente@qa.com",
        "password": "teste",
        "administrador": "true"
    }

@when("eu faço uma requisição POST para /usuarios")
def step_impl(context):
    context.response = requests.post(f"{BASE_URL}/usuarios", json=context.payload)

@then('a mensagem deve ser "{mensagem}"')
def step_impl(context, mensagem):
    response_json = context.response.json()
    assert response_json.get("message") == mensagem, f"Esperado: '{mensagem}', Recebido: '{response_json.get('message')}'"

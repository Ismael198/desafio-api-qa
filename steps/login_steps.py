from behave import given, when, then
import requests
from tests.config import BASE_URL

LOGIN_ENDPOINT = f"{BASE_URL}/login"

@given("que eu tenho um email e senha válidos")
def step_impl(context):
    context.payload = {
        "email": "fulano@qa.com",
        "password": "teste"
    }

@given("que eu tenho um email válido e senha inválida")
def step_impl(context):
    context.payload = {
        "email": "fulano@qa.com",
        "password": "senha_errada"
    }

@when("eu faço uma requisição POST para /login")
def step_impl(context):
    context.response = requests.post(
        LOGIN_ENDPOINT,
        json=context.payload,
        headers={
            "accept": "application/json",
            "Content-Type": "application/json"
        }
    )

@then("o status code deve ser {status_code}")
def step_impl(context, status_code):
    assert context.response.status_code == int(status_code), \
        f"Status code incorreto. Esperado: {status_code}, Recebido: {context.response.status_code}"

@then("a resposta deve conter um token de autorização")
def step_impl(context):
    assert "authorization" in context.response.json(), \
        f"Token não encontrado na resposta: {context.response.text}"

@then('a mensagem de erro deve ser "{mensagem}"')
def step_impl(context, mensagem):
    assert context.response.json()["message"] == mensagem, \
        f"Mensagem incorreta. Esperado: '{mensagem}', Recebido: '{context.response.json()['message']}'"
# tests/config.py
import requests

BASE_URL = "https://serverest.dev"
LOGIN_ENDPOINT = f"{BASE_URL}/login"

# Credenciais válidas do ServeRest
VALID_CREDENTIALS = {
    "email": "fulano@qa.com",
    "password": "teste"
}

def get_auth_token(email="fulano@qa.com", password="teste"):
    try:
        response = requests.post(
            f"{BASE_URL}/login",
            json={"email": email, "password": password},
            headers={
                "accept": "application/json",
                "Content-Type": "application/json"
            }
        )
        response.raise_for_status()
        token = response.json().get("authorization")
        if not token:
            raise ValueError("Token não retornado na resposta")
        return token
    except Exception as e:
        print(f"Erro ao obter token: {str(e)}")
        print(f"Resposta completa: {response.text if 'response' in locals() else 'N/A'}")
        raise
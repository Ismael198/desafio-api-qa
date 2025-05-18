# Testes BDD - Gerenciamento de Usuários

Este projeto utiliza o framework [Behave](https://behave.readthedocs.io/en/stable/) para testes automatizados BDD (Behavior-Driven Development) de uma API de gerenciamento de usuários.

## 📁 Estrutura do Projeto

desafio-api-qa/
├── features/
│   ├── __init__.py
│   ├── login.feature
│   ├── usuarios.feature
│   ├── produtos.feature
│   └── carrinhos.feature
├── steps/
│   ├── __init__.py   
│   ├── login_steps.py
│   ├── usuarios_steps.py
│   ├── produtos_steps.py
│   └── carrinhos_steps.py
├── tests/
│   ├── __init__.py
│   └── config.py/
├── README.md
└── requirements.txt

markdown
Copiar
Editar

## ✅ Requisitos

- Python 3.10+
- pip
- virtualenv (opcional, mas recomendado)

## ⚙️ Instalação

```bash
pip install -r requirements.txt
▶️ Executando os Testes
bash
Copiar
Editar
behave features/usuarios.feature
🧪 Levantamento de Cenários
Feature: Gerenciamento de Usuários
Como um administrador
Quero gerenciar usuários
Para controlar acessos ao sistema

Cenário 1: Criar usuário com dados válidos
Dado que eu tenho um novo usuário com email único
Quando eu faço uma requisição POST para /usuarios
Então o status code deve ser 201
E a mensagem deve ser "Cadastro realizado com sucesso"
Cenário 2: Tentar criar usuário com email duplicado
Dado que eu tenho um usuário com email já existente
Quando eu faço uma requisição POST para /usuarios
Então o status code deve ser 400
E a mensagem deve ser "Este email já está sendo usado"

📄 Licença
Este projeto está licenciado sob a licença MIT.# desafio-api-qa

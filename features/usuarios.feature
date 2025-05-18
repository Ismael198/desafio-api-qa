# features/usuarios.feature
Feature: Gerenciamento de Usuários
  Como um administrador
  Quero gerenciar usuários
  Para controlar acessos ao sistema

  Scenario: Criar usuário com dados válidos
    Given que eu tenho um novo usuário com email único
    When eu faço uma requisição POST para /usuarios
    Then o status code deve ser 201
    And a mensagem deve ser "Cadastro realizado com sucesso"

  Scenario: Tentar criar usuário com email duplicado
    Given que eu tenho um usuário com email já existente
    When eu faço uma requisição POST para /usuarios
    Then o status code deve ser 400
    And a mensagem deve ser "Este email já está sendo usado"
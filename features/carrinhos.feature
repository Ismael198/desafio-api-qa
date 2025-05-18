# features/carrinhos.feature
Feature: Gerenciamento de Carrinhos
  Como um usuário autenticado
  Quero gerenciar meu carrinho
  Para finalizar compras

  Scenario: Adicionar produto ao carrinho
    Given que eu tenho um token de usuário válido
    And um produto existente no catálogo
    When eu faço uma requisição POST para /carrinhos
    Then o status code deve ser 201

  Scenario: Tentar criar carrinho com produto inexistente
    Given que eu tenho um token de usuário válido
    And um produto com ID inválido
    When eu faço uma requisição POST para /carrinhos
    Then o status code deve ser 400

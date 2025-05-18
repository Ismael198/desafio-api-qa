Feature: Gerenciamento de Produtos
  Como um usuário autenticado
  Quero gerenciar produtos
  Para atualizar o catálogo

  Scenario: Adicionar produto com token válido
    Given que o usuário esteja autenticado com "fulano@qa.com" e "teste"
    When ele envia os dados do produto
    Then o produto é adicionado com sucesso
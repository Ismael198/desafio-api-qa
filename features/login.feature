Feature: Login no ServeRest
  Como um usuário do sistema
  Quero realizar login
  Para acessar funcionalidades protegidas

  Scenario: Login com credenciais válidas
    Given que eu tenho um email e senha válidos
    When eu faço uma requisição POST para /login
    Then o status code deve ser 200
    And a resposta deve conter um token de autorização

  Scenario: Login com senha inválida
    Given que eu tenho um email válido e senha inválida
    When eu faço uma requisição POST para /login
    Then o status code deve ser 401
    And a mensagem de erro deve ser "Email e/ou senha inválidos"
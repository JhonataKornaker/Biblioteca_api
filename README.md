# API Biblioteca

Desenvolvimento de Plano de Testes de software da api Biblioteca.

## Descrição dos Testes

- **Testes de Usuários**:
    - `test_cadastrar_usuario_sucesso`: Verifica se um usuário é cadastrado com sucesso.
    - `test_cadastrar_usuario_falha`: Verifica se o sistema impede o cadastro de uma matrícula duplicada.
    - `test_login_sucesso`: Verifica a autenticação de login com sucesso.
    - `test_login_falha`: Verifica a autenticação de login com senha invalida.

**Testes de Usuários**:
    - `test_cadastrar_livro`: Verifica se um livro é cadastrado corretamente no sistema.
    - `test_emprestar_livro`: Verifica se um livro pode ser emprestado corretamente e se o sistema impede o empréstimo de um livro já emprestado.
    - `test_devolver_livro`: Verifica se um livro pode ser devolvido corretamente e se o sistema impede a devolução de um livro já disponível.
    - `test_consultar_livro`: Verifica se um livro pode ser consultado corretamente e se o sistema lida com a consulta de um livro inexistente.
    - `test_alterar_livro`: Verifica se as informações de um livro podem ser alteradas corretamente e se o sistema lida com a alteração de um livro inexistente.
    - `test_excluir_livro`: Verifica se um livro pode ser excluído corretamente e se o sistema lida com a exclusão de um livro inexistente.

## Como Executar os Testes

```bash

git clone https://github.com/JhonataKornaker/Biblioteca_api.git
cd biblioteca_api
pip install -r requirements.txt
pytest

```
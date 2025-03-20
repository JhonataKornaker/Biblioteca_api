import pytest
from biblioteca.livros import (
    cadastrar_livro, emprestar_livro, devolver_livro, 
    consultar_livro, excluir_livro, alterar_livro, livros_db
)
from biblioteca.usuarios import cadastrar_usuario, login, usuarios_db

@pytest.fixture(autouse=True)
def limpar_banco():
    usuarios_db.clear()
    livros_db.clear()

def test_cadastrar_livro_regressao():
    # Testando cadastro de livro novamente após a modificação
    resultado, mensagem = cadastrar_livro("001", "Livro 001", "Autor 001")
    assert resultado == True and mensagem == "Cadastro realizado com sucesso"

    # Testando se o sistema não permite duplicação de livros
    resultado, mensagem = cadastrar_livro("001", "Livro 001", "Autor 001")
    assert resultado == False and mensagem == "Livro já cadastrado"

# Teste de alteração de livro (verificar se continua funcionando)
def test_alterar_livro_regressao():
    cadastrar_livro("002", "Livro 002", "Autor 002")
    resultado, mensagem = alterar_livro("002", "Livro 002 Alterado", "Autor 002")
    assert resultado == True and mensagem == "Livro alterado com sucesso."

# Teste de empréstimo de livro (verificar se não houve impacto na funcionalidade)
def test_emprestar_livro_regressao():
    cadastrar_livro("003", "Livro 003", "Autor 003")
    resultado, mensagem = emprestar_livro("003")
    assert resultado == True and mensagem == "Emprestimo realizado com sucesso."

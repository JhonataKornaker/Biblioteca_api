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

def test_aceitacao():

    # 🟢 Cenário: Cadastro e login do usuário
    assert cadastrar_usuario("123456", "Jhonata", "123jho") is True
    sucesso, mensagem = login("123456", "123jho")
    assert sucesso and mensagem == "Login bem-sucedido"

    # 🟢 Cenário: Cadastro e manipulação de um livro
    sucesso, mensagem = cadastrar_livro("001", "Livro 001", "Autor 001")
    assert sucesso and mensagem == "Cadastro realizado com sucesso"
    assert "001" in livros_db

    # 🟢 Cenário: Empréstimo e devolução do livro
    sucesso, mensagem = emprestar_livro("001")
    assert sucesso and mensagem == "Emprestimo realizado com sucesso."
    assert not livros_db["001"]["disponivel"]

    sucesso, mensagem = devolver_livro("001")
    assert sucesso is True and mensagem == "Devolução realizada com sucesso."
    assert livros_db["001"]["disponivel"]

    # 🟢 Cenário: Consultas e alteração do livro
    sucesso, livro = consultar_livro("001")
    assert sucesso is True
    assert livro == {"titulo": "Livro 001", "autor": "Autor 001", "disponivel": True}

    sucesso, mensagem = alterar_livro("001", titulo="Livro 002")
    assert sucesso and mensagem == "Livro alterado com sucesso."
    assert livros_db["001"]["titulo"] == "Livro 002"

    # 🟢 Cenário: Exclusão do livro
    sucesso, mensagem = excluir_livro("001")
    assert sucesso and mensagem == "Livro excluído da biblioteca com sucesso."
    assert "001" not in livros_db

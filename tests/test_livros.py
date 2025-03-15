import pytest
from biblioteca.livros import cadastrar_livro, emprestar_livro, devolver_livro, consultar_livro, excluir_livro, alterar_livro, livros_db

def test_cadastrar_livro():
    assert cadastrar_livro("001", "Livro 001", "Autor 001") == (True, "Cadastro realizado com sucesso")
    assert "001" in livros_db

def test_emprestar_livro():
    assert emprestar_livro("001") == (True, "Emprestimo realizado com sucesso.")
    assert livros_db["001"]["disponivel"] == False

    with pytest.raises(ValueError, match="Livro ja emprestado"):
        emprestar_livro("001")

def test_devolver_livro():
    assert devolver_livro("001") == True
    assert livros_db["001"]["disponivel"] == True

    with pytest.raises(ValueError, match="Livro ja esta disponivel"):
        devolver_livro("001")

def test_consultar_livro():
    livro = consultar_livro("001")
    assert livro["titulo"] == "Livro 001"

    with pytest.raises(ValueError, match="Livro nao encontrado"):
        consultar_livro("999")

def test_alterar_livro():
    assert alterar_livro("001", titulo="Livro 002") == (True, "Livro alterado com sucesso.")
    assert livros_db["001"]["titulo"] == "Livro 002"

    with pytest.raises(ValueError, match="Livro não encontrado."):
        alterar_livro("999", titulo="Livro não encontrado.")

def test_excluir_livro():
    assert excluir_livro("001") == (True, "Livro excluido da biblioteca com sucesso.")
    assert "001" not in livros_db

    with pytest.raises(ValueError, match="Livro não encontrado."):
        excluir_livro("002")

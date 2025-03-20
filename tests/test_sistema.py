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

def test_sistema():

    # ✅ Teste de fluxo correto
    assert cadastrar_usuario("123456", "Jhonata", "123jho") is True
    assert cadastrar_livro("001", "Livro 001", "Autor 001") == (True, "Cadastro realizado com sucesso")

    # ✅ Testando tentativa de login com senha errada
    sucesso, mensagem = login("123456", "senha_errada")
    assert not sucesso and mensagem == "Senha incorreta"

    # ✅ Testando cadastro de livro duplicado
    sucesso, mensagem = cadastrar_livro("001", "Livro Repetido", "Autor X")
    assert not sucesso and mensagem == "Livro já cadastrado"

    # ✅ Testando empréstimo de um livro inexistente
    sucesso, mensagem = emprestar_livro("999")
    assert not sucesso and mensagem == "Livro não encontrado"

    # ✅ Testando devolução de um livro que não foi emprestado
    sucesso, mensagem = devolver_livro("001") 
    assert not sucesso and mensagem == "Livro já está disponível." 

    # ✅ Testando alteração de livro inexistente
    sucesso, mensagem = alterar_livro("999", titulo="Novo Título")
    assert not sucesso and mensagem == "Livro não encontrado"

    # ✅ Testando exclusão de um livro inexistente
    sucesso, mensagem = excluir_livro("999")
    assert not sucesso and mensagem == "Livro não encontrado"

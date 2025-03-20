import pytest
from biblioteca.livros import (
    cadastrar_livro, emprestar_livro, devolver_livro, 
    consultar_livro, excluir_livro, alterar_livro, livros_db
)
from biblioteca.usuarios import cadastrar_usuario, login, usuarios_db

@pytest.fixture(autouse=True)
def limpar_banco():
    livros_db.clear()
    usuarios_db.clear()

def test_cadastrar_livro():
    sucesso, mensagem = cadastrar_livro("001", "Livro 001", "Autor 001")
    assert sucesso and mensagem == "Cadastro realizado com sucesso"
    assert "001" in livros_db

    sucesso, mensagem = cadastrar_livro("001", "Livro Duplicado", "Autor X")
    assert not sucesso and mensagem == "Livro já cadastrado"

def test_consultar_livro():
    livros_db["001"] = {"titulo": "Livro 001", "autor": "Autor 001", "disponivel": True}

    sucesso, livro = consultar_livro("001")
    assert sucesso is True
    assert livro == {"titulo": "Livro 001", "autor": "Autor 001", "disponivel": True}

    sucesso, mensagem = consultar_livro("999")
    assert not sucesso and mensagem == "Livro não encontrado"

def test_emprestar_livro():
    livros_db["001"] = {"titulo": "Livro 001", "autor": "Autor 001", "disponivel": True}

    sucesso, mensagem = emprestar_livro("001")
    assert sucesso and mensagem == "Emprestimo realizado com sucesso."
    assert not livros_db["001"]["disponivel"]

    sucesso, mensagem = emprestar_livro("001")
    assert not sucesso and mensagem == "Livro já emprestado."

def test_devolver_livro():
    livros_db["001"] = {"titulo": "Livro 001", "autor": "Autor 001", "disponivel": False}

    sucesso, mensagem = devolver_livro("001")
    assert sucesso and mensagem == "Devolução realizada com sucesso."
    assert livros_db["001"]["disponivel"]

    sucesso, mensagem = devolver_livro("001")
    assert not sucesso and mensagem == "Livro já está disponível."

def test_excluir_livro():
    livros_db["001"] = {"titulo": "Livro 001", "autor": "Autor 001", "disponivel": True}

    sucesso, mensagem = excluir_livro("001")
    assert sucesso and mensagem == "Livro excluído da biblioteca com sucesso."
    assert "001" not in livros_db 

    sucesso, mensagem = excluir_livro("001")
    assert not sucesso and mensagem == "Livro não encontrado"

def test_alterar_livro():
    livros_db["001"] = {"titulo": "Livro 001", "autor": "Autor 001", "disponivel": True}

    # Alterando título e autor
    sucesso, mensagem = alterar_livro("001", titulo="Novo Título", autor="Novo Autor")
    assert sucesso and mensagem == "Livro alterado com sucesso."
    assert livros_db["001"]["titulo"] == "Novo Título"
    assert livros_db["001"]["autor"] == "Novo Autor"

    # Alterando apenas o título
    sucesso, mensagem = alterar_livro("001", titulo="Título Atualizado")
    assert sucesso and mensagem == "Livro alterado com sucesso."
    assert livros_db["001"]["titulo"] == "Título Atualizado"
    assert livros_db["001"]["autor"] == "Novo Autor"

    # Alterando apenas o autor
    sucesso, mensagem = alterar_livro("001", autor="Autor Atualizado")
    assert sucesso and mensagem == "Livro alterado com sucesso."
    assert livros_db["001"]["titulo"] == "Título Atualizado"
    assert livros_db["001"]["autor"] == "Autor Atualizado"

    # Tentando alterar um livro inexistente
    sucesso, mensagem = alterar_livro("999", titulo="Teste")
    assert not sucesso and mensagem == "Livro não encontrado"

def test_cadastrar_usuario():

    # Cadastro de um novo usuário
    assert cadastrar_usuario("123456", "Jhonata", "123jho") is True
    assert "123456" in usuarios_db
    assert usuarios_db["123456"]["nome"] == "Jhonata"
    assert usuarios_db["123456"]["senha"] == "123jho"

    # Tentativa de cadastrar um usuário com a mesma matrícula
    sucesso, mensagem = cadastrar_usuario("123456", "Outro Nome", "outrasenha")
    assert not sucesso and mensagem == "Matricula ja cadastrada"


def test_login():
    usuarios_db["123456"] = {"nome": "Jhonata", "senha": "123jho"}

    # Login correto
    sucesso, mensagem = login("123456", "123jho")
    assert sucesso is True and mensagem == "Login bem-sucedido"

    # Login com senha incorreta
    sucesso, mensagem = login("123456", "senha_errada")
    assert sucesso is False and mensagem == "Senha incorreta"

    # Tentativa de login com usuário inexistente
    sucesso, mensagem = login("999999", "qualquersenha")
    assert sucesso is False and mensagem == "Usuário não encontrado"

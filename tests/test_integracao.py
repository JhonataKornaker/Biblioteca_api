import pytest
from biblioteca.livros import cadastrar_livro, emprestar_livro, devolver_livro, consultar_livro, excluir_livro, alterar_livro, livros_db
from biblioteca.usuarios import cadastrar_usuario, login, usuarios_db

@pytest.fixture(autouse=True)
def limpar_banco():
    usuarios_db.clear()
    livros_db.clear()

def test_integracao_cadastrar_e_login():

    # ✅ Cadastro e login devem funcionar juntos corretamente
    assert cadastrar_usuario("123456", "Jhonata", "123jho") is True
    sucesso, mensagem = login("123456", "123jho")
    assert sucesso is True and mensagem == "Login bem-sucedido"

def test_integracao_livro_usuario():

    # ✅ Passo 1: Cadastrar usuário
    assert cadastrar_usuario("123", "João", "senha123") is True 

    # ✅ Passo 2: Cadastrar livro
    resultado, mensagem = cadastrar_livro("001", "Python para Iniciantes", "Autor X")
    assert resultado is True, "O cadastro do livro falhou"
    assert mensagem == "Cadastro realizado com sucesso"

    # ✅ Passo 3: Consultar livro (deve estar disponível)
    sucesso, livro = consultar_livro("001")
    assert sucesso is True
    assert livro["disponivel"] is True

    # ✅ Passo 4: Usuário faz login
    sucesso, mensagem = login("123", "senha123")
    assert sucesso is True and mensagem == "Login bem-sucedido"

    # ✅ Passo 5: Usuário empresta o livro
    sucesso, mensagem = emprestar_livro("001")
    assert sucesso is True and mensagem == "Emprestimo realizado com sucesso."

    # ✅ Passo 6: Consultar livro novamente (agora deve estar indisponível)
    sucesso, livro = consultar_livro("001")
    assert sucesso is True
    assert livro["disponivel"] is False

    # ✅ Passo 7: Usuário devolve o livro
    sucesso, mensagem = devolver_livro("001")
    assert sucesso is True and mensagem == "Devolução realizada com sucesso."

    # ✅ Passo 8: Consultar livro novamente (deve estar disponível)
    sucesso, livro = consultar_livro("001")
    assert sucesso is True
    assert livro["disponivel"] is True

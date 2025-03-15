import pytest
from biblioteca.usuarios import cadastrar_usuario, login, usuarios_db

def test_cadastrar_usuario():
    assert cadastrar_usuario("123456", "Jhonata", "123jho") == True 
    assert '123456' in usuarios_db  

    with pytest.raises(ValueError, match="Matricula já cadastrada."):
        cadastrar_usuario("123456", "Jhonata", "123jho")

def test_login_sucesso():
    assert login("123456", "123jho") == (True, "Login bem-sucedido")

def test_login_falha():
    assert login("123456", "senha_errada") == "Senha incorreta"
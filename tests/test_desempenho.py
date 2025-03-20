import pytest
from biblioteca.livros import (
    cadastrar_livro, emprestar_livro, devolver_livro, 
    consultar_livro, excluir_livro, alterar_livro, livros_db
)
from biblioteca.usuarios import cadastrar_usuario, login, usuarios_db

@pytest.fixture(autouse=True)
def limpar_banco_de_dados():
    livros_db.clear()
    usuarios_db.clear()

# 🔥 Cadastrar 5.000 livros rapidamente
def test_desempenho_cadastrar_livros(benchmark):
    def cadastrar_varios():
        for i in range(5000):
            cadastrar_livro(str(i), f"Livro {i}", f"Autor {i}")
    benchmark(cadastrar_varios)
    assert len(livros_db) == 5000

# 🔥 Emprestar 5.000 livros
def test_desempenho_emprestar_livros(benchmark):
    for i in range(5000):
        cadastrar_livro(str(i), f"Livro {i}", f"Autor {i}")
    
    def emprestar_varios():
        for i in range(5000):
            emprestar_livro(str(i))
    
    benchmark(emprestar_varios)

# 🔥 Devolver 5.000 livros
def test_desempenho_devolver_livros(benchmark):
    for i in range(5000):
        cadastrar_livro(str(i), f"Livro {i}", f"Autor {i}")
        emprestar_livro(str(i))

    def devolver_varios():
        for i in range(5000):
            devolver_livro(str(i))

    benchmark(devolver_varios)

# 🔥 Consultar 5.000 livros
def test_desempenho_consultar_livros(benchmark):
    for i in range(5000):
        cadastrar_livro(str(i), f"Livro {i}", f"Autor {i}")

    def consultar_varios():
        for i in range(5000):
            consultar_livro(str(i))

    benchmark(consultar_varios)

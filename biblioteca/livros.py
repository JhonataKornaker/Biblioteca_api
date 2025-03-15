livros_db = {}

def cadastrar_livro(id_livro, titulo, autor, disponivel=True):
    if id_livro in livros_db:
        raise ValueError("Livro já cadastrado.")
    livros_db[id_livro] = {"titulo": titulo, "autor": autor, "disponivel": disponivel}
    return True, "Cadastro realizado com sucesso"

def emprestar_livro(id_livro):
    livro = livros_db.get(id_livro)
    if not livro:
        raise ValueError("Livro nao encontrado")
    if not livro["disponivel"]:
        raise ValueError("Livro ja emprestado")
    livro["disponivel"] = False
    return True, "Emprestimo realizado com sucesso."

def devolver_livro(id_livro):
    livro = livros_db.get(id_livro)
    if not livro:
        raise ValueError("Livro nao encontrado")
    if livro["disponivel"]:
        raise ValueError("Livro ja esta disponivel")
    livro["disponivel"] = True
    return True

def consultar_livro(id_livro):
    livro = livros_db.get(id_livro)
    if not livro:
        raise ValueError("Livro nao encontrado")
    return livro

def excluir_livro(id_livro):
    if id_livro not in livros_db:
        raise ValueError("Livro não encontrado.")
    del livros_db[id_livro]
    return True, "Livro excluido da biblioteca com sucesso."

def alterar_livro(id_livro, titulo=None, autor=None):
    livro = livros_db.get(id_livro)
    if not livro:
        raise ValueError("Livro não encontrado.")
    if titulo is not None:
        livro["titulo"] = titulo
    if autor is not None:
        livro["autor"] = autor
    
    return True, "Livro alterado com sucesso." 

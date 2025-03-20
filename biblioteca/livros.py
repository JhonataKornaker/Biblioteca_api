livros_db = {}

def cadastrar_livro(id_livro, titulo, autor, disponivel=True):
    if id_livro in livros_db:
        return False, "Livro já cadastrado"
    livros_db[id_livro] = {"titulo": titulo, "autor": autor, "disponivel": disponivel}
    return True, "Cadastro realizado com sucesso"

def emprestar_livro(id_livro):
    livro = livros_db.get(id_livro)
    if not livro:
        return False, "Livro não encontrado"
    if not livro["disponivel"]:
        return False, "Livro já emprestado."
    livro["disponivel"] = False
    return True, "Emprestimo realizado com sucesso."

def devolver_livro(id_livro):
    livro = livros_db.get(id_livro)
    if not livro:
        return False, "Livro não encontrado"
    if livro["disponivel"]:
        return False, "Livro já está disponível."
    livro["disponivel"] = True
    return True, "Devolução realizada com sucesso."

def consultar_livro(id_livro):
    livro = livros_db.get(id_livro)
    if not livro:
        return False, "Livro não encontrado"
    return True, livro

def excluir_livro(id_livro):
    if id_livro not in livros_db:
        return False, "Livro não encontrado"
    del livros_db[id_livro]
    return True, "Livro excluído da biblioteca com sucesso."

def alterar_livro(id_livro, titulo=None, autor=None):
    livro = livros_db.get(id_livro)
    if not livro:
        return False, "Livro não encontrado"
    if titulo is not None:
        livro["titulo"] = titulo
    if autor is not None:
        livro["autor"] = autor
    return True, "Livro alterado com sucesso."

usuarios_db = {}

def cadastrar_usuario(matricula, nome, senha):
    if matricula in usuarios_db:
        return False, "Matricula ja cadastrada"
    usuarios_db[matricula] = {"nome": nome, "senha": senha}
    return True

def login(matricula, senha):
    usuario = usuarios_db.get(matricula)
    
    if not usuario:
        return False, "Usuário não encontrado"
    
    if usuario["senha"] != senha:
        return False, "Senha incorreta"
    
    return True, "Login bem-sucedido"
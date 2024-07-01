import livros_e_usuarios_disponíveis

def adicionar_usuarios():
    print("Qual seu nome? ", end=" ")
    nome = input()
    livros_e_usuarios_disponíveis.usuarios.append(nome)
    usuario = livros_e_usuarios_disponíveis.usuarios[-1]
    print(f"Usuário {usuario} adicionado com sucesso")
    #return usuario
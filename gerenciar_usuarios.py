import livros_e_usuarios_disponíveis

class Usuarios:

    def adicionar_usuarios():
        print("Qual seu nome? ", end=" ")
        nome = input()
        livros_e_usuarios_disponíveis.usuarios.append(nome)
        usuario = livros_e_usuarios_disponíveis.usuarios[-1]
        print(f"Usuário {usuario} adicionado com sucesso!")
        return usuario
    
    def exibir_usuario():
        print("-"*30)
        print("usuários cadastrados:")
        print("-"*30)
        for indice, usuario in enumerate(livros_e_usuarios_disponíveis.usuarios, start=1):
            print(f"{indice} - {usuario}\n")

    def pesquisar_usuario(user):
        temp_user = ""
        for indice, usuario in enumerate(livros_e_usuarios_disponíveis.usuarios):
            if(usuario == user):
                temp_user = usuario
        if temp_user == "":
            print("Esse nome não foi encontrado na base de dados. Vamos cadastrá-lo")
            temp_user = Usuarios.adicionar_usuarios()
        return temp_user
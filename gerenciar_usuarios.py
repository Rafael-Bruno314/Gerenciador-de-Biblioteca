import intermedio_db
import json
import time

class Usuarios:

    def adicionar_usuarios(nome) -> str:
        with open("usuarios.txt", "r", encoding='utf-8',errors='ignore') as arquivo:
            db_antes = arquivo.read()
            db_antes = db_antes[:-1]
        with open("usuarios.txt", "w", encoding='utf-8',errors='ignore') as write_arquivo:
            write_arquivo.write(db_antes + "," + json.dumps(nome, ensure_ascii=False) + "]")
        usuario = usuarios_db()[-1]
        time.sleep(1)
        print(f"Usuário {usuario} adicionado com sucesso!")
        return usuario
    
    def exibir_usuario():
        print("-"*30)
        print("usuários cadastrados:")
        print("-"*30)
        for indice, usuario in enumerate(usuarios_db(), start=1):
            print(f"{indice} - {usuario}\n")

    def pesquisar_usuario(user):
        temp_user = ""
        for indice, usuario in enumerate(usuarios_db()):
            if(usuario == user):
                temp_user = usuario
        if temp_user == "":
            print("Esse nome não foi encontrado na base de dados. Vamos cadastrá-lo")
            time.sleep(3)
            temp_user = Usuarios.adicionar_usuarios(user)
        return temp_user


def usuarios_db() -> list:
    with open("usuarios.txt", "r", encoding='utf-8') as arquivo:
        conteudo = arquivo.read()
        lista_de_users = json.loads(conteudo)
    return lista_de_users
